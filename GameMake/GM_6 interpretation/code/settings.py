level_map = [
'                            ',
'                            ',
'                            ',
' XX    XXX            XX    ',
' XX P                       ',
' XXXX       XX           XX ',
' XXXX      XX               ',
' XX    X  XXXX    XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']
# level_map : 공부하기 위한 맵 수작업으로 만들기 -> X : 타일, P : player가 있을 위치

tile_size = 64                                  # tile_size : tiled에서 만든 한 칸의 사이즈
screen_width = 1200                             # 화면 넓이
screen_height = len(level_map) * tile_size      # 화면 높이