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
            