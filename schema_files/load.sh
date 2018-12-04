#!/bin/bash
export PGPASSWORD=docker
export PGHOST=localhost
export PGUSER=docker
export PGPORT=5432
export PGDB=healthyrivers

psql -h $PGHOST -U $PGUSER  -p $PGPORT -c "drop database $PGDB;" gis
psql -h $PGHOST -U $PGUSER  -p $PGPORT -c "create database $PGDB;" gis
pg_restore -W -p $PGPORT -h $PGHOST -U $PGUSER -d $PGDB ~/Google\ Drive/1-Kartoza/Projects/FreshwaterResearchCentre/FBIS/OldFreshwaterDatabase/OldDatabaseDumpInPostgresFormat/rivers_db.dump 

psql -h $PGHOST  -p $PGPORT -U $PGUSER -f schema_migrations.sql $PGDB
