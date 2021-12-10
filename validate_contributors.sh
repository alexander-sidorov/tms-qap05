#!/usr/bin/env bash

# ---------------------------------------------------------
abort() {
  if test -n "$1"; then
    echo >&2 -e "\n\nFAILED: $1\n\n"
  fi
  exit 1
}

trap 'abort' 0

set -e
set -o pipefail

# ---------------------------------------------------------

function contains() {
    local n=$#
    local value=${!n}
    for ((i=1; i < $#; i++)) {
        if [ "${!i}" == "${value}" ]; then
            echo "y"
            return 0
        fi
    }
    echo "n"
    return 1
}

assert_names() {
  dir_names=$(ls -d hw/* | sed -e 's/hw\///g')
  github_names=(
    "alexander_sidorov"
    "andrei_bondar"
    "andrey_yelin"
    "denis_asipenko"
    "kirill_tobolich"
    "maksim_ptitski"
    "maria_saganovich"
    "nikita_pakhomov"
    "sasha_yaroshevich"
    "siarhei_apanel"
    "tatsiana_kukharskaya"
    "vadim_maletski"
    "valeriya_mavritskaya"
    "vlad_yancharski"
    "yaroslav_belaychuk"
  )

  for n in ${dir_names}; do
    if [[ $n == "__init__.py" ]]; then
      continue;
    fi

    if [[ $(contains "${github_names[@]}" "$n") == "n" ]]; then
      echo "unknown contributor name in hw/: '$n'"
      return 1
    fi

    pkg_init_py="hw/$n/__init__.py"
    if [[ ! -f $pkg_init_py ]]; then
      echo "File $pkg_init_py MUST be added"
      return 1
    fi
  done
}

# ---------------------------------------------------------

rm -rf hw/__pycache__

# checks

assert_names || abort "MESS WITH CONTRIBUTORS NAMES"

# ---------------------------------------------------------
trap : 0
# ---------------------------------------------------------
