# OS, sys, fnmatch - Convertendo videos com Python - FFMPEG
# https://ffmpeg.zeranoe.com/builds/

"""
ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac-b:a 320k -c:s srt -map v:0 -map a -map 1:0 "SAIDA"
"""

import os
import fnmatch
import sys

if sys.platform == 'linux': # verifica a plataforma (sisterma operacional)
    comando_ffmpeg = 'fnmpeg'
else:
    comando_ffmpeg = r'ffmpeg\ffmpeg.exe' # para windows - contando que o arquivo .exe tenha sido baixado de aconrdo com o link no topo e salvo dentro da pasta desde script
    
codec_video = 'libx264'
codec_audio = 'aac'
crf = '-crf 23'
preset = '-preset ultrafast'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'

caminho_origem = '/home/diegopolicarpo/Estudos/Python/Udemy/Python_3_do_basico_ao_avancado/POO/aula136/videos'
caminho_destino = '/home/diegopolicarpo/Estudos/Python/Udemy/Python_3_do_basico_ao_avancado/POO/aula136/saida'

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mp4'):
            continue
        
        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.str'
        
        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''
            print('Vídeo sem legenda.')
            
        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
        
        # Caso queira salvar na mesma pasta de origem
        """
        nome_do_arquivo = nome_arquivo + '_NOVO' + extensao_arquivo
        arquivo_saida = os,path.join(raiz, nome_novo_arquivo)
        """
        arquivo_saida = f'{caminho_destino}/{nome_arquivo}_NOVO{extensao_arquivo}'
        
        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda}' \
            f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio}' \
            f'{debug} {map_legenda} "{arquivo_saida}"'
            
        os.system(comando)