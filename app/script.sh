#!/usr/bin/bash

# SOLARA_APP=ui.pages flask run --host=0.0.0.0
cd ui && solara run ui.pages --host=0.0.0.0
# tail -f /dev/null