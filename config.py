screen_width = 800
screen_height = 600
background_image = 'images/background.jpg'

frame_rate = 90

row_count = 6
brick_width = 60
brick_height = 20
brick_color = "#c2a3ba"
offset_y = brick_height + 10

ball_speed = 3
ball_radius = 8
ball_color = "#8BC29A"

paddle_width = 80
paddle_height = 20
paddle_color = "#c8d8d9"
paddle_speed = 6

status_offset_y = 5

text_color = "#788186"
initial_lives = 3
lives_right_offset = 85
lives_offset = screen_width - lives_right_offset
score_offset = 5

font_name = 'Comic Sans MS'
font_size = 18

effect_duration = 20

sounds_effects = dict(
    brick_hit='sound_effects/brick_hit.wav',
    effect_done='sound_effects/effect_done.wav',
    paddle_hit='sound_effects/paddle_hit.wav',
    level_complete='sound_effects/level_complete.wav',
)

message_duration = 2

button_text_color = "#FFFFFF"
button_normal_back_color = "#aba3c2"
button_hover_back_color = "#89829b"
button_pressed_back_color = "#676274"

menu_offset_x = 20
menu_offset_y = 300
menu_button_w = 80
menu_button_h = 50
