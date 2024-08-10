import os
import argparse
import subprocess
import ffmpeg

def reassemble_exo_files(directory, output_file):
    #Création des répertoire -o 
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Création des répertoires manquants: {output_dir}")
    
    # Trouver et trier tous les fichiers EXO 
    exo_files = sorted([f for f in os.listdir(directory) if f.endswith('.exo')])
    
    # Ouverture des fichiers 
    with open(output_file, 'wb') as outfile:
        for exo_file in exo_files:
            exo_path = os.path.join(directory, exo_file)
            print(f"Ajout du fichier {exo_file} à {output_file}")
            with open(exo_path, 'rb') as infile:
                # Lecture des EXO
                outfile.write(infile.read())

    print(f"Reconstitution terminée. Fichier final : {output_file}")

def repair_with_ffmpeg(input_file, output_file):
    try:
        # FFMPEG pour les fichiers corrompus
        ffmpeg.input(input_file).output(output_file, c='copy').run()
        print(f"Vidéo réparée ou convertie : {output_file}")
    except ffmpeg.Error as e:
        print(f"Erreur lors de la réparation avec ffmpeg: {e}")

def verify_output_file(output_file):
    
    if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
        print(f"Le fichier {output_file} a été créé avec succès et semble valide.")
    else:
        print(f"Erreur : Le fichier {output_file} n'a pas pu être créé correctement.")

def main():
   
    parser = argparse.ArgumentParser(description="Reconstituer et réparer des fichiers EXO en un fichier vidéo.")
    parser.add_argument('-i', '--input', required=True, help="Répertoire d'entrée contenant les fichiers EXO.")
    parser.add_argument('-o', '--output', required=True, help="Chemin complet du fichier vidéo de sortie.")
    parser.add_argument('-r', '--repair', action='store_true', help="Réparer le fichier vidéo avec ffmpeg après reconstitution.")
    
    args = parser.parse_args()

    
    reassemble_exo_files(args.input, args.output)
    
    
    verify_output_file(args.output)
    
    
    if args.repair:
        repaired_output_file = args.output.replace('.mp4', '_fixed.mp4')
        repair_with_ffmpeg(args.output, repaired_output_file)

if __name__ == "__main__":
    main()
