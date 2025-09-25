{ pkgs, ... }:
pkgs.mkShell {
  nativeBuildInputs = with pkgs.buildPackages; [
    uv
    python3
    python3.pkgs.myst-parser
    python3.pkgs.pip
    python3.pkgs.pipx
    python3.pkgs.pytest
    python3.pkgs.sphinx
    python3.pkgs.sphinx-book-theme
    python3.pkgs.tox
    python3.pkgs.virtualenv
    python3.pkgs.virtualenvwrapper
    python3.pkgs.rich
  ];
}
