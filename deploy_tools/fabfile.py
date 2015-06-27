from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run, prefix
import random

env.use_ssh_config = True

REPO_URL = 'https://github.com/Locky1138/superlists.git'

def deploy():
    site_folder = '/home/%s/sites/%s' % (env.user, env.host)
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)

def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ('database', 'static', 'source'):
        run('mkdir -p %s/%s' % (site_folder, subfolder))

def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):
        run('cd %s && git fetch' % (source_folder,))
    else:
        run('git clone %s %s' % (REPO_URL, source_folder))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('cd %s && git reset --hard %s' % (source_folder, current_commit))

def _update_settings(source_folder, site_name):
    settings_path = source_folder + '/superlists/settings.py'
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path,
        'ALLOWED_HOSTS = .+$',
        'ALLOWED_HOSTS = ["%s"]' % (site_name,)
    )
    secret_key_file = source_folder + '/superlists/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_+'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, "SECRET_KEY = '%s'" % (key,))
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')

def _update_virtualenv(source_folder):
    virtualenv_folder = source_folder + '/../virtualenv'
    if not exists('miniconda3/'):
        # Install miniconda3
        run('wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda3.sh')
        run('bash miniconda3.sh -b')
    if not exists('miniconda3/envs/superlists/'):
        # create conda virtualenv
        with prefix('cd %s' % (source_folder,)):
            run('$PWD/miniconda3/bin/conda env create')
    if not exists(virtualenv_folder + '/bin/python'):
        # create symlink virtualenv > conda env
        # ln -s /home/locky/miniconda3/envs/superlists sites/staging.locky1138.com/virtualenv
        run('ln -s $PWD/miniconda3/envs/superlists %s' % virtual_env_folder)
    run('%s/bin/conda env update -e superlists -f %s/environment.yml' % (virtualenv_folder, source_folder))
#    with prefix('cd %s && source activate superlists' % (source_folder,)):
#        run('conda env update')

def _update_static_files(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py collectstatic --noinput' % source_folder)

def _update_database(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py migrate --noinput' % source_folder)
