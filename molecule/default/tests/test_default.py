"""
Role unit tests
"""


def test_motd(host):
    """
    Ensures that motd advertisements are removed
    """
    pkg = host.package('motd-news-config')
    units = [
        'motd-news.service',
        'motd-news.timer'
    ]

    assert not pkg.is_installed
    for _unit in units:
        _out = host.run("systemctl status %s", _unit).stdout.strip().lower()
        assert "loaded: masked" in _out


def test_snap(host):
    """
    Ensure that Snapcraft is removed
    """
    # check that directories are removed
    dirs = [
        '/snap',
        '/var/snap',
        '/var/lib/snapd'
    ]
    for _dir in dirs:
        assert not host.file(_dir).exists
        assert not host.file(_dir).is_directory

    # check that packages are removed
    pkgs = [
        'snap',
        'snapd'
    ]
    for _pkg in pkgs:
        assert not host.package(_pkg).is_installed

    # check for snapd apt preference
    _pref = host.file('/etc/apt/preferences.d/no-snap.pref')
    assert _pref.exists
    assert _pref.contains("Package: snapd")
    assert _pref.contains("Pin-Priority: -1")


def test_apt(host):
    """
    Ensure that APT advertisement is removed
    """
    # ensure templates and hooks are removed
    files = [
        '/var/lib/ubuntu-advantage/messages/apt-pre-invoke-no-packages-apps.tmpl',  # noqa: 501
        '/var/lib/ubuntu-advantage/messages/apt-pre-invoke-packages-apps.tmpl',
        '/etc/apt/apt.conf.d/20apt-esm-hook.conf'
    ]
    for _file in files:
        assert not host.file(_file).exists

    # double-check that apt doesn't contain Ubuntu Pro bullshit messages
    with host.sudo():
        _apt = host.run("apt-get update").stdout.strip().lower()
        assert "tRy uBuNtu pRo".lower() not in _apt
