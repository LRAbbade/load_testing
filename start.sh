#!/bin/bash
LOCUS_OPTS="--host=$LOCUST_TARGET_HOST -L DEBUG"
# LOCUST_MODE=${LOCUST_MODE:-standalone}

if [[ "$LOCUST_MODE" = "master" ]]; then
    LOCUS_OPTS="$LOCUS_OPTS --master"
elif [[ "$LOCUST_MODE" = "worker" ]]; then
    LOCUS_OPTS="$LOCUS_OPTS --slave --master-host=$LOCUST_MASTER"
fi

echo "locust $LOCUS_OPTS"
locust $LOCUS_OPTS
