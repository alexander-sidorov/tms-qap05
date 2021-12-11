#!/usr/bin/env bash

contributor=$1
shift 1

pr=$1
shift 1

workdir=
name=

case "${contributor}" in
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

#for f in "$@"; do
#  ok=$(echo "${f}" | grep "^${workdir}")
#  if [[ -z "${ok}" ]]; then
#    echo "file $f is outside ${contributor}'s working directory ${workdir}"
#    exit 1
#  fi
#done

pr_ok=$(echo "${pr}" | grep "^${name} - Lesson \\d\+")
if [[ -z "${pr_ok}" ]]; then
  echo "Pull request title MUST be in form '<first name> <last name> - Lesson <number>'"
  exit 1
fi
