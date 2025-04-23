#!/bin/sh
# Download the trino-cli to a writable directory like /tmp
curl -o /tmp/trino-cli https://repo1.maven.org/maven2/io/trino/trino-cli/447/trino-cli-447-executable.jar
chmod +x /tmp/trino-cli

# Add /tmp to PATH for this session
export PATH=$PATH:/tmp

# Start the Trino server
trino-server --server http://localhost:8080 --catalog hive --schema default
