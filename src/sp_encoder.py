import sentencepiece as spm

g_return_token = 'Й'


class Encoder:
    def __init__(self, sp):
        self.sp = sp

    def encode(self, text):
        return self.sp.EncodeAsIds(text)

    def decode(self, tokens):
        return self.sp.DecodeIds([int(token) for token in tokens]).replace(g_return_token, '\n')


def get_encoder(sp_model_file):
    sp = spm.SentencePieceProcessor()
    sp.load(sp_model_file)
    return Encoder(sp)

