'''
一次改掉全部組態
matplotlib.rcParams.update({'font.size': 22})

matplotlib.rcParams.裡面是一個dict : 
RcParams({'_internal.classic_mode': False,
          'agg.path.chunksize': 0,
          'animation.avconv_args': [],
          'animation.avconv_path': 'avconv',
          'animation.bitrate': -1,
          'animation.codec': 'h264',
          'animation.convert_args': [],
裡面都是組態類的東西
'''

# 一次修正所有字型，針對單個圖
# bigger_font = {'font.size':22}
# with plt.rc_context(bigger_font):
#   Do your plot

# plt.rc_context : 是一個物件，顯然可以處理暫時性的組態
