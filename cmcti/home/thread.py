import threading
from django.core.mail import send_mail
from register.models import CustomUser


class SendEmailThread(threading.Thread):

    def __init__(self, titulo):
        self.titulo = titulo
        threading.Thread.__init__(self)
    

    def run(self):
        try:
            print('Enviando emails')
            usuarios = CustomUser.objects.all()
            for user in usuarios:
                send_mail(
                    'Nova demanda cadastrada na plataforma CMCTI',
                    f'Nova demanda/documento "{str(self.titulo)}" cadastrada(o)\nAcesse a '+
                    'plataforma para mais informações\n\nSistema CMCTI',
                    'cmctisistema@gmail.com',
                    [f'{user.email}'],
                    fail_silently=False,
                )
        except Exception as e:
            print(e)
'''
send_mail(
            'Requisição para NOVO INSTRUTOR',
            f'Nome: {str(nome)}\nSobre o minicurso: {str(info_minicurso)}\nInformações do instrutor: {str(sobre_voce)}\nEmail Instrutor: {str(request.user.email)}',
            'wtic@ufjnet.net',
            ['wtic@ufjnet.net'],
            fail_silently=False,
        )

'''