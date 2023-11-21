import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg") # 練習１：背景画像Surfaceの生成
    kk_img = pg.image.load("ex01/fig/3.png") # 練習２：こうかとん画像Surfaceの生成
    kk_img = pg.transform.flip(kk_img, True, False) # 練習２：こうかとんの左右反転
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)] # 練習３：こうかとんSurfaceのリスト
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0]) # 練習４：背景画像の表示
        screen.blit(kk_imgs[tmr%2], [300, 200]) # 練習５：こうかとんはばたく
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()