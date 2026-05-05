    while True:
        if ball.hit_bottom:
            canvas.create_text(500, 400, text="GAME OVER", fill="white", font=("Helvetica", 32))
            root.update()
            break

        root.update()
        ball.movement()
        paddle.get_pos()

        ball_pos = ball.coords()
        paddle_pos = canvas.coords(paddle.rec)
        if ball.collision(ball_pos, paddle_pos):
            ball.bounce()

        for brick in bricks:
            if brick.collision(ball_pos):
                brick.broken()
                ball.bounce()
                break

        sleep(0.003)