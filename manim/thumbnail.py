from manim import *

class Thumbnail(Scene):
    def construct(self):
        wheel = SVGMobject("img/cannon-wheel-brown.svg").scale(0.925).rotate(PI/6).set_z_index(5)
        barrel = SVGMobject("img/cannon-barrel-grey.svg").scale(2).shift(1.5*RIGHT+1.25*UP)
        cannon = VGroup(wheel,barrel).shift(5*LEFT+2*DOWN)

    
        background_lines = VGroup(Line(start=3.55*LEFT+2*DOWN,end=14*RIGHT+2*DOWN,color=WHITE),
                                  Line(start=14*LEFT+2*DOWN,end=6*LEFT+2*DOWN,color=WHITE)).set_opacity(0.5)

        angle = Arc(radius=1.5,start_angle=PI/6+0.175,angle=-PI/6-0.175,color=GRAY_C).move_arc_center_to(4*LEFT+2.5*DOWN)
        theta = Tex(r"$\theta$",color=GRAY_C).move_to(1.75*DL+0.2*UP+0.5*LEFT)
        dotted_line = DashedLine(start=2.5*DOWN+4.2*LEFT,end=2.5*DOWN+2.5*LEFT,color=GRAY)

        def dot_curve(x):
            return -0.15*(x+2)**2 + 0.75*x + 1.3

        dots = VGroup()
        for i in range(7):
            dots.add(Dot(color=WHITE,fill_opacity=0.7).scale(2).move_to(RIGHT*(i-1)+UP*dot_curve(i-1)))

        self.add(background_lines,cannon,dotted_line,dots,angle,theta)