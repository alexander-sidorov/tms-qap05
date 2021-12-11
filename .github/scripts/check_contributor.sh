#!/usr/bin/env bash

contributor=$1
shift 1
workdir=

case "${contributor}" in
"alexander-sidorov")
  workdir="alexander_sidorov"
  ;;
"Andrei9325")
  workdir="andrei_bondar"
  ;;
"Zyola")
  workdir="andrey_yelin"
  ;;
"denisasipenko")
  workdir="denis_asipenko"
  ;;
"Tobkirill")
  workdir="kirill_tobolich"
  ;;
"MaksimPtitski")
  workdir="maksim_ptitski"
  ;;
"maryiasa")
  workdir="maria_saganovich"
  ;;
"Brlinetta")
  workdir="nikita_pakhomov"
  ;;
"SashaYaroshevich")
  workdir="sasha_yaroshevich"
  ;;
"APOSHAml")
  workdir="siarhei_apanel"
  ;;
"Tatsikuk26")
  workdir="tatsiana_kukharskaya"
  ;;
"vadison90125")
  workdir="vadim_maletski"
  ;;
"lerkin011")
  workdir="valeriya_mavritskaya"
  ;;
"Yancharski")
  workdir="vlad_yancharski"
  ;;
"YaroslavBelaychuk")
  workdir="yaroslav_belaychuk"
  ;;
esac

if [[ -z ${workdir} ]]; then
  echo "unknown contributor ${contributor}"
  exit 1
fi

workdir="hw/${workdir}/"

for f in "$@"; do
  ok=$(echo "${f}" | grep "^${workdir}")
  if [[ -z "${ok}" ]]; then
    echo "file $f is outside ${contributor}'s working directory ${workdir}"
    exit 1
  fi
done
