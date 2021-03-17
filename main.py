def on_on_created(sprite):
    sprite.set_position(randint(0, 160), 0)
    sprite.set_bounce_on_wall(True)
    sprite.set_velocity(32, 18)
sprites.on_created(SpriteKind.enemy, on_on_created)

def on_a_pressed():
    global projectile
    if len(sprites.all_of_kind(SpriteKind.projectile)) < Maximum_bullets_on_screen:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 2 2 . . . . . . . 
                            . . . . . . . 2 2 . . . . . . . 
                            . . . . . . 2 2 2 2 . . . . . . 
                            . . . . . . 2 2 2 2 . . . . . . 
                            . . . . . . 2 2 2 2 . . . . . . 
                            . . . . . . 2 2 2 2 . . . . . . 
                            . . . . . . 2 5 4 2 . . . . . . 
                            . . . . . 2 5 4 5 5 2 . . . . . 
                            . . . . . . . 5 4 . . . . . . . 
                            . . . . . . . 4 5 . . . . . . .
            """),
            mySprite,
            0,
            -71)
        music.pew_pew.play()
        projectile.start_effect(effects.trail, 200)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def Create_Player():
    global mySprite
    mySprite = sprites.create(assets.image("""
        Rocket 1
    """), SpriteKind.player)
    controller.move_sprite(mySprite)
    mySprite.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . c d . . . . . . . 
                        . . . . . . . c d . . . . . . . 
                        . . . . . . . c d . . . . . . . 
                        . . . . . . . c b . . . . . . . 
                        . . . . . . . f f . . . . . . . 
                        . . . . . . . c 4 . . . . . . . 
                        . . . . . . . f f . . . . . . . 
                        . . . . . . . e 4 . . . . . . . 
                        . . . . . . e e 5 2 . . . . . . 
                        . . . . . . e 4 5 2 . . . . . . 
                        . . . . . c c c 2 2 2 . . . . . 
                        . . . . e e 4 4 4 5 2 2 . . . . 
                        . . e f f f c c 2 2 f f 2 2 . . 
                        . e e e e 2 2 4 4 4 4 5 4 2 2 . 
                        e e e e e e 2 2 4 4 4 5 4 4 2 2 
                        e e e e e e 2 2 4 4 4 4 5 4 2 2
            """),
            img("""
                . . . . . . . c d . . . . . . . 
                        . . . . . . . c d . . . . . . . 
                        . . . . . . . c d . . . . . . . 
                        . . . . . . . c b . . . . . . . 
                        . . . . . . . f f . . . . . . . 
                        . . . . . . . c 3 . . . . . . . 
                        . . . . . . . f f . . . . . . . 
                        . . . . . . . 8 3 . . . . . . . 
                        . . . . . . 8 8 1 a . . . . . . 
                        . . . . . . 8 3 1 a . . . . . . 
                        . . . . . c c c a a a . . . . . 
                        . . . . 8 8 3 3 3 1 a a . . . . 
                        . . 8 f f f c c a a f f a a . . 
                        . 8 8 8 8 a a 3 3 3 3 1 3 a a . 
                        8 8 8 8 8 8 a a 3 3 3 1 3 3 a a 
                        8 8 8 8 8 8 a a 3 3 3 3 1 3 a a
            """),
            img("""
                . . . . . . . c d . . . . . . . 
                        . . . . . . . c d . . . . . . . 
                        . . . . . . . c d . . . . . . . 
                        . . . . . . . c b . . . . . . . 
                        . . . . . . . f f . . . . . . . 
                        . . . . . . . c 6 . . . . . . . 
                        . . . . . . . f f . . . . . . . 
                        . . . . . . . 8 6 . . . . . . . 
                        . . . . . . 8 8 9 8 . . . . . . 
                        . . . . . . 8 6 9 8 . . . . . . 
                        . . . . . c c c 8 8 8 . . . . . 
                        . . . . 8 8 6 6 6 9 8 8 . . . . 
                        . . 8 f f f c c e e f f 8 8 . . 
                        . 8 8 8 8 8 8 6 6 6 6 9 6 8 8 . 
                        8 8 8 8 8 8 8 8 6 6 6 9 6 6 8 8 
                        8 8 8 8 8 8 8 8 6 6 6 6 9 6 8 8
            """)],
        500,
        True)

def on_life_zero():
    game.over(False, effects.splatter)
info.on_life_zero(on_life_zero)

def on_on_destroyed(sprite):
    if info.life() > 0:
        pause(2000)
        Create_Player()
sprites.on_destroyed(SpriteKind.player, on_on_destroyed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy(effects.fire, 500)
    music.small_crash.play()
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    sprite.destroy(effects.fire, 500)
    music.small_crash.play()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

mySprite: Sprite = None
projectile: Sprite = None
Maximum_bullets_on_screen = 0
info.set_life(3)
Maximum_bullets_on_screen = 3
number_of_baddies = 5
effects.star_field.start_screen_effect()
Create_Player()

def on_forever():
    if len(sprites.all_of_kind(SpriteKind.enemy)) < number_of_baddies:
        sprites.all_of_kind(SpriteKind.enemy).append(sprites.create(img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . 8 8 . . . . . . . 
                                . . . . . . 8 8 8 8 . . . . . . 
                                . . . . . 8 8 8 8 8 8 . . . . . 
                                . . . . 8 8 8 8 8 8 8 8 . . . . 
                                . . . . 8 8 8 8 8 8 8 8 . . . . 
                                . . . 8 8 8 2 8 8 2 8 8 8 . . . 
                                . . . 8 8 8 8 8 8 8 8 8 8 . . . 
                                . . . 8 8 8 8 8 8 8 8 8 8 . . . 
                                . . . 8 8 8 8 8 8 8 8 8 8 . . . 
                                . . . 8 8 8 8 2 2 8 8 8 8 . . . 
                                . . . 8 8 8 2 8 8 2 8 8 8 . . . 
                                . . . 8 8 8 8 8 8 8 8 8 8 . . . 
                                . . . 8 . . 8 . . 8 . 8 . . . . 
                                . . . . 8 . 8 . 8 . . . 8 . . . 
                                . . . 8 . . 8 . . 8 . 8 . . . .
                """),
                SpriteKind.enemy))
    pause(randint(1000, 5000))
forever(on_forever)
