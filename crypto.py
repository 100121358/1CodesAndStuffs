# transposistion cipher

# Original: This_is_a_secret_message_I_want_to_Transmit
# From_Roger_the_Assassin
# encrypted:hsi_ertmsaeta_att_rnmtti_sace_esg_htiwn_otasi
# fo_rgr_te_sasn

def scrambled2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
            charCount = charCount + 1
            cipherText = oddChars + evenChars
            return cipherText

def scramble2Decrypt(cipherText):
    halfLength = len(cipherText)// 2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plaintext = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

        if len(oddChars0) < len(evenChars):
            plainText = plainText + evenChars[-1]

            return plainText

def encryptMessage():
    msg = 