# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Voto

# @receiver(post_save, sender=Voto)
# def update_candidato_votes(sender, instance, created, **kwargs):
#     # Solo actuamos cuando se crea el voto
#     if created:
#         # Incrementa en 1 el campo votos de cada candidato asociado
#         candidato1 = instance.candidato1
#         candidato2 = instance.candidato2

#         candidato1.votos += 1
#         candidato1.save(update_fields=['votos'])

#         candidato2.votos += 1
#         candidato2.save(update_fields=['votos'])
