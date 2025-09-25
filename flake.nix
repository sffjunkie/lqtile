{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    { nixpkgs, ... }:
    let
      forAllSystems = nixpkgs.lib.genAttrs [
        "aarch64-linux"
        "x86_64-darwin"
        "x86_64-linux"
      ];
    in
    {
      devShells = forAllSystems (
        system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
        in
        {
          default = pkgs.mkShell {
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
          };
        }
      );

      formatter = forAllSystems (system: nixpkgs.legacyPackages.${system}.nixfmt-rfc-style);
    };
}
