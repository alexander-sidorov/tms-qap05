#!/usr/bin/env bash

contributor=$1
shift 1

pr=$1
shift 1

workdir=
name=

case "${contributor}" in
"tgrx")
  workdir="tgrx"
  name="TG RX"
  ;;
"alexander-sidorov")
  workdir="alexander_sidorov"
  name="Alexander Sidorov"
  ;;
"Andrei9325")
  workdir="andrei_bondar"
  name="Andrei Bondar"
  ;;
"Zyola")
  workdir="andrey_yelin"
  name="Andrey Yelin"
  ;;
"denisasipenko")
  workdir="denis_asipenko"
  name="Denis Asipenko"
  ;;
"Tobkirill")
  workdir="kirill_tobolich"
  name="Kirill Tobolich"
  ;;
"MaksimPtitski")
  workdir="maksim_ptitski"
  name="Maksim Ptitski"
  ;;
"maryiasa")
  workdir="maria_saganovich"
  name="Maria Saganovich"
  ;;
"Brlinetta")
  workdir="nikita_pakhomov"
  name="Nikita Pakhomov"
  ;;
"SashaYaroshevich")
  workdir="sasha_yaroshevich"
  name="Sasha Yaroshevich"
  ;;
"APOSHAml")
  workdir="siarhei_apanel"
  name="Siarhei Apanel"
  ;;
"Tatsikuk26")
  workdir="tatsiana_kukharskaya"
  name="Tatsiana Kukharskaya"
  ;;
"vadison90125")
  workdir="vadim_maletski"
  name="Vadim Maletski"
  ;;
"lerkin011")
  workdir="valeriya_mavritskaya"
  name="Valeriya Mavritskaya"
  ;;
"Yancharski")
  workdir="vlad_yancharski"
  name="Vlad Yancharski"
  ;;
"YaroslavBelaychuk")
  workdir="yaroslav_belaychuk"
  name="Yaroslav Belaychuk"
  ;;
esac

if [[ -z ${workdir} ]]; then
  echo "unknown contributor ${contributor}"
  exit 1
fi

workdir="hw/${workdir}/"
qa_workdir="hw/_qa/"

allowed_files=(
  .gitignore
  .github/scripts/check_contributor.sh
  .github/workflows/contributing.yaml
)

for file in "$@"; do
  file_in_hw=$(echo "${file}" | grep "^${workdir}")
  file_in_qa=$(echo "${file}" | grep "^${qa_workdir}")

  if [[ -n "${file_in_qa}" ]]; then
    ok="ok"

  elif [[ -z "${file_in_hw}" ]]; then
    ok=

    for allowed_file in ${allowed_files[*]}; do
      if [[ "${file}" == "${allowed_file}" ]]; then
        ok="ok"
        break
      fi
    done

    if [[ -z "${ok}" ]]; then
      echo "file $file is not acceptable:"
      echo -e "    it is outside ${contributor}'s working directory '${workdir}'"
      echo -e "    and is not one of allowed: ${allowed_files[*]}"
      exit 1
    fi
  fi
done

pr_ok=$(echo "${pr}" | grep "^${name} - Lesson")
if [[ -z "${pr_ok}" ]]; then
  echo "Malformed pull request title: '${pr}'"
  echo "Pull request title MUST be in form '<first name> <last name> - Lesson <number>'"
  exit 1
fi
