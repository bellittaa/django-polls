from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    nickname = models.CharField(max_length=100)
    avatar = models.CharField(max_length=225, null=True, blank=True)
    usuariocol = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.nome


class Questionario(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    questionariocol = models.CharField(max_length=45, default='NOW()')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Hashtag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag


class Questionario_has_Hashtag(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('questionario', 'hashtag'),)
