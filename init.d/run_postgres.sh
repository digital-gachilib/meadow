#!/bin/bash
docker run --name=meadow_db --rm -d -v dmd_postgres_data:/var/lib/postgresql/data -p 5432:5432 -e POSTGRES_HOST_AUTH_METHOD=trust postgres
# default username: postgres
# default password: '' or 'postgres'
