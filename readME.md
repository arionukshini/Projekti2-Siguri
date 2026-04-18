Implementimi i One time pad duke gjeneruar nje key stream nga nje int32 ose string seed. Implementimi i SymmetricAlgorithm qe ofron enkriptues dhe dekriptues per kete algoritem.

Ky projekt paraqet implementimin e algoritmit One Time Pad ne gjuhen Python. Qellimi i projektit eshte te tregoje menyren se si nje tekst i thjeshte mund te enkriptohet dhe pastaj te dekriptohet duke perdorur nje key stream.

One Time Pad eshte nje metode e enkriptimit ku secila pjese e mesazhit kombinohet me nje pjese te celesit. Ne kete projekt, key stream gjenerohet automatikisht nga nje seed. Seed mund te jete nje numer `int32` ose nje tekst `string`.

I njejti seed perdoret gjate enkriptimit dhe dekriptimit. Kjo ben qe gjate dekriptimit te gjenerohet i njejti key stream dhe teksti i enkriptuar te kthehet perseri ne tekstin origjinal.

Projekti funksionon si algoritëm simetrik, sepse i njejti seed perdoret per te dy proceset: enkriptim dhe dekriptim.