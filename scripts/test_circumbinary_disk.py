import sys

sys.path.insert(1, ".")

from sailfish.setups.circumbinary_disk import CircumbinaryDisk


def main():
    setup = CircumbinaryDisk(which_diagnostics="mdots")
    checkpoint_data = setup.checkpoint_diagnostics(0.0)

    assert checkpoint_data["diagnostics"] == setup.diagnostics
    assert len(checkpoint_data["diagnostics"]) == 3
    assert len(checkpoint_data["point_masses"]) == 2


if __name__ == "__main__":
    main()
