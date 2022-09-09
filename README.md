# decanonical

Removes Canonical bloatware such as **Snap** and `motd-news` from Ubuntu installations.

## Requirements

No requirements.

## Role Variables

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `decanonical_purge_motd` | `true` | Purges MOTD advertisements |
| `decanonical_purge_snap` | `true` | Purge Snaps and Snapcraft stack |
| `decanonical_purge_unneeded_pkgs` | `false` | Removes unneeded packages |
| `decanonical_unneeded_pkgs` | *see [`defaults`](defaults/main.yml)* | Packages to remove |

## Dependencies

No dependencies.

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: stdevel.decanonical
```

## License

BSD

## Author Information

Christian Stankowic
