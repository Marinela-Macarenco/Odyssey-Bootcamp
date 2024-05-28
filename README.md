# Odyssey-Bootcamp
Porsche  Fan Platform

hey ! hey! Înainte de a testa acest proiect va fi nevoie să faci un virtual enviroment.Iată pașii de creare + activare virtual enviroment(pentru Windows),
În terminal scrim următoarele comenzi( Între aceste bare "|" este scrisă comanda , deci în terminal scrim fără ele):
Prima comandă este |python -m venv tutorial-env| tastăm enter
A doua comandă este |Test-Path -Path "tutorial-env\Scripts" |tastăm enter
|cd tutorial-env\Scripts| tastăm enter
|Get-ChildItem| tastăm enter
|Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process| tastăm enter
|.\Activate.ps1| tastăm enter

După ce am creat + activat virtual enviroment , instalăm bibliotecile care sunt descrise în requirements.txt.

!!Înainte de a testa aplicația deschidem un terminal nou ( facem run la fișierul porsche.py), deschidem alt terminal nou și scrim comanda |streamlit run main.py|.
Făcând cunoștință cu interfața de la aplicație , rog să se atragă atenția la următoarele aspecte:
!Unele pagini au nevoie de mai mult timp ca să își încarce interfața
!Pagina cu reviews necesită mai mult timp de rulare ,adăugarea unui nou review pe pagină merge!! ->după ce apare o casetă mai jos unde spune că review-ul a fost adăugat cu  succes , trebuie să faceți un refresh la pagină , după care dacă accesați pagina cu reviews veți putea vedea review-ul vostru adăugat (nu ezitați să-l căutați în tabel), also dacă scrolați tabelul la dreapta o să observați că un AI stabilește emoția comentariului.

Pe pagina "Hidden" sunt 3 butoane într-un rând  , pe ele puteți da click!

Succes!






 
