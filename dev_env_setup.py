import subprocess
import sys

java = 'java'
maven = 'mvn'
scala = 'scala'
gradle = 'gradle'
vagrant = 'vagrant'

tools = [java, maven, scala, gradle]

brew = "brew"

version = "-version"
version_alt = "--version"

# to be used later
install_latest_version_java = None
install_latest_version_maven = None
install_latest_version_scala = None


# end


def check_tool_version(tool):
    tool_version = subprocess.check_output([tool, version], stderr=subprocess.STDOUT)
    if tool_version != '':
        print "" + tool.upper() + " is already installed "
    else:
        print '' + tool.upper() + ' is not installed on this machine. Installing the latest version of ' + tool.upper()
        try:
            p = subprocess.call(["brew cask install " + tool], shell=True)
        except OSError:
            print "" + tool + " was not installed."
            raise


def check_brew_version():
    tool_version = subprocess.check_output([brew, version_alt], stderr=subprocess.STDOUT)
    if tool_version != '':
        print "Brew is already installed "
    else:
        print "Brew is not installed. Installing brew "
        command = "mkdir ~/homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew"
        subprocess.call([command])


def check_vagrant_version():
    is_vagrant_installed = 1
    try:
        tool_version = subprocess.check_output([vagrant, version_alt], stderr=subprocess.STDOUT)
    except OSError:
        is_vagrant_installed = 0

    if is_vagrant_installed == 1:
        print "Vagrant is already installed "
    else:
        print "Vagrant is not installed. Installing vagrant "
        try:
            p = subprocess.call(["brew cask install virtualbox vagrant vagrant-manager"], shell=True)
        except OSError:
            print "Vagrant was not installed."
            raise


def install_java_11_macos():
    print "Installing Java 11..."
    try:
        subprocess.call(["brew install java11"], shell=True)
    except OSError:
        print "Java 11 was not installed"
        exit(1)
    print "Java 11 was successfully installed"


def uninstall_java_11():
    print "Uninstalling Java 11..."

    print "Uninstalling Java 11 was successful"


def check_os():
    current_os = sys.platform
    print("You are running " + current_os)


def main():
    check_os()
    check_brew_version()
    check_vagrant_version()
    for t in tools:
        check_tool_version(t)


main()
# test
# install_java_11_macos()
