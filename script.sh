#!/bin/bash

install_depends() {
    yum install -y libffi-devel zlib-devel bzip2-devel git \
               readline-devel sqlite-devel wget curl llvm \
               ncurses-devel openssl-devel lzma-sdk-devel \
               redhat-rpm-config net-tools vim
}

install_pyenv() {
    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
}

configure_bashrc() {
    echo '  export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    ' >> ~/.bashrc
    cat ~/.bashrc
    source ~/.bashrc
}

# See available versions of python
#pyenv install -l

install_environments_py() {
    pyenv install 2.7.17
    pyenv install 3.8.0
}

# Choose version
#pyenv global 3.8.0
	
create_virt_envs_py() {
    pyenv virtualenv 2.7.17 venv2.7.17
    pyenv virtualenv 3.8.0 venv3.8.0
    mkdir venv2.7 && $(echo 'Virtualenv directory' > venv2.7/README)
    mkdir venv3.8 && $(echo 'Virtualenv directory' > venv3.8/README)
}

install_depends
install_pyenv
configure_bashrc
install_environments_py
create_virt_envs_py
/vagrant/py_script.py