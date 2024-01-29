#!/bin/bash

for directory in "$(pwd)"/*; do
    if [ -d $directory ]; then
        for file in "$directory"/*.py; do
            if [ -f "$file" ]; then
                if ! head -n 1 "$file" | grep -q "#!/usr/bin/python3"; then
                    # Ajouter le shebang au début du fichier
                    echo "#!/usr/bin/python3" | cat - "$file" > temp && mv temp "$file"
                    # Rendre le fichier exécutable
                    chmod +x "$file"
                    echo "Shebang ajouté à $file"
                else
                    echo "Shebang déjà présent dans $file"
                fi
            fi
        done
    fi
done
