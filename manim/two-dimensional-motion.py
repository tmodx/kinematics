from manim import *

def set_math_colors(*equations):
    for equation in equations:
        equation.set_color_by_tex("{g}",GRAY)
        equation.set_color_by_tex("{x}",RED)
        equation.set_color_by_tex("{y}",RED)
        equation.set_color_by_tex("{r}",RED)
        equation.set_color_by_tex("{s}",RED)
        equation.set_color_by_tex("{v}",BLUE)
        equation.set_color_by_tex("{a}",GREEN)
        equation.set_color_by_tex("omega",BLUE)

class MotionIn2D(Scene):
    def construct(self):
        ax = Axes(
            x_range = [0,10,1],
            y_range = [0,5,1],
            tips=True
        ).scale(0.5).move_to(ORIGIN)

        ax_labels = ax.get_axis_labels(x_label = Tex("$x$"),y_label = Tex("$y$"))

        system = VGroup(Square(side_length=1.5,fill_color=BLUE,color=BLUE,fill_opacity=0.05),Dot(color=WHITE))

        self.play(FadeIn(ax),Write(ax_labels),rate_func=rate_functions.smooth,run_time=1)
        self.wait()
        self.play(VGroup(ax,ax_labels).animate.scale(2).move_to(ORIGIN),Write(system))

        coordinates = always_redraw(lambda: Tex(f"$({ax.p2c(system.get_center())[0]:.2f},{ax.p2c(system.get_center())[1]:.2f})$").next_to(system,UP)) 

        system_vector = Vector(RIGHT,color=RED)
        system_vector.add_updater(lambda mob: mob.put_start_and_end_on(ax.get_origin(),system.get_center()))
        
        self.play(FadeIn(coordinates))
        self.wait()
        self.play(system.animate.shift(2*RIGHT+0.1*DOWN),rate_func=rate_functions.smooth)
        self.play(system.animate.shift(3*LEFT),rate_func=rate_functions.smooth)
        self.wait()
        self.play(system.animate.shift(2*UP+0.1*LEFT),rate_func=rate_functions.smooth)
        self.play(system.animate.shift(2.5*DOWN+0.1*RIGHT),rate_func=rate_functions.smooth)
        self.wait()
        
        coordinates_vectorized = always_redraw(lambda: Tex(f"$<{ax.p2c(system.get_center())[0]:.2f},{ax.p2c(system.get_center())[1]:.2f}>$").next_to(system,UP)) 
        self.play(FadeIn(system_vector),FadeOut(coordinates),FadeIn(coordinates_vectorized)) 
        self.remove(coordinates)
        self.play(system.animate.shift(LEFT),rate_func=rate_functions.ease_in_out_sine)
        self.play(system.animate.shift(UP),rate_func=rate_functions.ease_in_out_sine)
        self.play(system.animate.shift(RIGHT),rate_func=rate_functions.ease_in_out_sine)
        self.play(system.animate.shift(DOWN),rate_func=rate_functions.ease_in_out_sine)
        self.wait()

        system_copy = system.copy()
        vector_label_copy = always_redraw(lambda: Tex(f"$<{ax.p2c(system_copy.get_center())[0]:.2f},{ax.p2c(system_copy.get_center())[1]:.2f}>$").next_to(system_copy,UP))
        system_copy_arrow = Vector(RIGHT,color=RED).add_updater(lambda mob: mob.put_start_and_end_on(ax.get_origin(),system_copy.get_center()))

        r1_label = Tex(r"$\vec{r_1}$",color=RED).move_to(3.5*LEFT+1.3*DOWN)
        r2_label = Tex(r"$\vec{r_2}$",color=RED).move_to(1.5*LEFT+2.3*DOWN)

        self.add(system_copy,vector_label_copy,system_copy_arrow)
        self.play(system_copy.animate.shift(4*RIGHT),FadeIn(r1_label,r2_label))

        delta_r = Vector(RIGHT,color=GREEN).put_start_and_end_on(system.get_center(),system_copy.get_center())
        delta_r_label = Tex(r"$\Delta \vec{r}$",color=GREEN).next_to(delta_r,UP)

        # The :.2f formats it to two decimal places. The difference between that and round() is that it ALWAYS keeps the second decimal,
        # so 3.1 will be "3.10."
        # This keeps the numbers from being jittery whenever the represented number could be represented by 2 digits.
        delta_r_equation = MathTex(r"\Delta \vec{r}","=",r"\vec{{r}_2}","-",r"\vec{{r}_1}","=",r"\ ",
                                    f"<{ax.p2c(system_copy.get_center())[0]:.2f}-{ax.p2c(system.get_center())[0]:.2f},{ax.p2c(system_copy.get_center())[1]:.2f}-{ax.p2c(system.get_center())[1]:.2f}>").shift(UP*2.5)
        delta_r_equation2 = MathTex(r"\Delta \vec{r}","=",r"\vec{{r}_2}","-",r"\vec{{r}_1}","=",r"\ ",
                                    f"<{(ax.p2c(system_copy.get_center())[0]-ax.p2c(system.get_center())[0]):.2f},{(ax.p2c(system_copy.get_center())[1]-ax.p2c(system.get_center())[1]):.2f}>").shift(UP*2.5)

        delta_r_equation.set_color_by_tex("Delta",GREEN)
        delta_r_equation2.set_color_by_tex("Delta",GREEN)

        set_math_colors(delta_r_equation,delta_r_equation2)

        self.play(GrowArrow(delta_r),FadeIn(delta_r_label))
        self.wait()

        delta_r_mobjects = VGroup(delta_r,delta_r_label).copy()

        self.play(Transform(delta_r_mobjects,delta_r_equation))
        self.wait()
        self.play(Transform(delta_r_mobjects,delta_r_equation2))
        self.wait()

        velocity_equation = MathTex(r"\vec{v}_{\text{avg}}","=",r"{\Delta \vec{r}",r"\over",r"\Delta t}","=",r"\frac{1}{\Delta t}",
                                    f"<{(ax.p2c(system_copy.get_center())[0]-ax.p2c(system.get_center())[0]):.2f},{(ax.p2c(system_copy.get_center())[1]-ax.p2c(system.get_center())[1]):.2f}>").shift(UP*2)
        
        acceleration_equation = MathTex(r"\vec{a}_{\text{avg}}","=",r"{\Delta \vec{v}",r"\over",r"\Delta t}").next_to(velocity_equation,DOWN)


        set_math_colors(velocity_equation,acceleration_equation)

        self.play(delta_r_mobjects.animate.shift(0.5*UP),FadeIn(velocity_equation))
        self.wait()
        self.play(FadeOut(system,system_copy,coordinates_vectorized,vector_label_copy,
                            delta_r, system_vector, system_copy_arrow,r1_label,r2_label,delta_r_label),
                    FadeIn(acceleration_equation))
        self.wait()
        self.play(FadeOut(ax,ax_labels),VGroup(delta_r_mobjects,velocity_equation,acceleration_equation).animate.move_to(ORIGIN))
        self.wait()

        velocity_simplified = MathTex(r"\vec{v}_{\text{avg}}","=",r"{\Delta \vec{r}",r"\over",r"\Delta t}").move_to(velocity_equation)
        delta_r_simplified = MathTex(r"\Delta \vec{r}","=",r"\vec{{r}_2}","-",r"\vec{{r}_1}").next_to(velocity_simplified,UP)

        set_math_colors(delta_r_simplified,velocity_simplified)

        self.play(Transform(delta_r_mobjects,delta_r_simplified),Transform(velocity_equation,velocity_simplified))
        self.wait()

        velocity_limit = MathTex(r"\vec{v}","=",r"\displaystyle \lim_{\Delta t \to 0}",r"{\Delta \vec{r}",r"\over",r"\Delta t}").move_to(velocity_simplified)
        acceleration_limit = MathTex(r"\vec{a}","=",r"\displaystyle \lim_{\Delta t \to 0}",r"{\Delta \vec{v}",r"\over",r"\Delta t}").next_to(velocity_limit,DOWN)
        set_math_colors(velocity_limit,acceleration_limit)

        self.play(Transform(velocity_equation,velocity_limit),Transform(acceleration_equation,acceleration_limit))
        self.wait()

class ComponentsOfVector(Scene):
    def construct(self):
        sample_vector = Vector(5*RIGHT+3*UP,color=ORANGE).move_to(ORIGIN)
        x_component = Vector(RIGHT,color=RED).put_start_and_end_on(sample_vector.get_start(),sample_vector.get_start()+5*RIGHT)
        y_component = Vector(UP,color=YELLOW_D).put_start_and_end_on(x_component.get_end(),x_component.get_end()+3*UP) 

        vector_label = MathTex(r"\vec{v}",color=ORANGE).shift(0.25*LEFT+0.5*UP)
        x_label = MathTex(r"\vec{v}_x",color=RED).next_to(x_component,DOWN)
        y_label = MathTex(r"\vec{v}_y",color=YELLOW_D).next_to(y_component,RIGHT)

        duck = SVGMobject("img/rubber-duck.svg").scale(0.15).next_to(y_component.get_end(),RIGHT).shift(0.075*DL+0.075*LEFT)

        self.play(GrowArrow(sample_vector),FadeIn(vector_label))
        self.play(Transform(sample_vector.copy(),x_component),GrowArrow(y_component),FadeIn(x_label,y_label),FadeIn(duck))
        self.wait()

class Cannon(Scene):
    def construct(self):
        wheel = SVGMobject("img/cannon-wheel.svg").scale(0.925).rotate(PI/6).set_z_index(5)
        barrel = SVGMobject("img/cannon-barrel.svg").scale(2).shift(1.5*RIGHT+1.25*UP)

        # self.add(NumberPlane())

        background_lines = VGroup(Line(start=3.55*LEFT+2*DOWN,end=14*RIGHT+2*DOWN,color=WHITE),
                                  Line(start=14*LEFT+2*DOWN,end=6*LEFT+2*DOWN,color=WHITE)).set_opacity(0.5)

        cannon = VGroup(wheel,barrel).shift(5*LEFT+2*DOWN)
        barrel.rotate(-PI/6,about_point=wheel.get_center())

        angle = Arc(radius=2,start_angle=PI/6+0.175,angle=-PI/6-0.175).move_arc_center_to(4*LEFT+2.5*DOWN)
        theta = Tex(r"$\theta$").move_to(1.75*DL+0.2*UP)

        initial_velocity_label = Tex(r"$\vec{v}_i$",color=BLUE).move_to(1.5*LEFT+UP)
        velocity_x_label = Tex(r"$\vec{v}_{i,x}$",color=TEAL).move_to(3*LEFT+3*DOWN)
        velocity_y_label = Tex(r"$\vec{v}_{i,y}$",color=PURPLE).move_to(DL)

        initial_velocity = Vector(RIGHT,color=BLUE).put_start_and_end_on(5*LEFT+2.5*DOWN,1.5*LEFT+0.25*UP+0.2*DOWN).set_z_index(10)
        velocity_x_component = Vector(RIGHT,color=TEAL).put_start_and_end_on(5*LEFT+2.5*DOWN,1.5*LEFT+2.5*DOWN)
        velocity_y_component = Vector(RIGHT,color=PURPLE).put_start_and_end_on(1.5*LEFT+2.5*DOWN,1.5*LEFT+0.25*UP+0.2*DOWN)

        def dot_curve(x):
            return -0.1*(x+2)**2 + 0.9*x + 1.5

        dots = VGroup()
        for i in range(9):
            dots.add(Dot(color=WHITE).scale(2).move_to(RIGHT*(i-1)+UP*dot_curve(i-1)))

        dotted_line = DashedLine(start=2.5*DOWN+4.2*LEFT,end=2.5*DOWN+2*LEFT)


        cosine_ratio = MathTex(r"\cos(\theta)","=","{a",r"\over","h}","=",r"{v_{i,x}",r"\over",r"v_i}").to_edge(UL)
        cosine_ratio.set_color_by_tex("{a",TEAL)
        cosine_ratio.set_color_by_tex("h}",BLUE)
        cosine_ratio.set_color_by_tex("v_i",BLUE)
        cosine_ratio.set_color_by_tex("v_{i,x}",TEAL)

        x_velocity_equation = MathTex("v_{i,x}","=","v_i",r"\cos(\theta)").next_to(cosine_ratio,DOWN)
        x_velocity_equation.set_color_by_tex("v_{i,x}",TEAL)
        x_velocity_equation.set_color_by_tex("v_i",BLUE)

        x_component_solution1 = MathTex("{x}(t)","=","{x}_i","+","v_{i,x}","t","+",r"\frac{1}{2}","{a}_x","t","^2").next_to(x_velocity_equation,DOWN).shift(0.5*RIGHT)
        x_component_solution1.set_color_by_tex("v",BLUE)

        x_component_solution2 = MathTex("{x}(t)","=","{x}_i","+","v_{i,x}","t","+",r"\frac{1}{2}","(0)","t","^2").move_to(x_component_solution1)
        x_component_solution2.set_color_by_tex("v",BLUE)

        x_component_solution3 = MathTex("{x}(t)","=","(0)","+","v_{i,x}","t","+",r"\frac{1}{2}","(0)","t","^2").move_to(x_component_solution2)
        x_component_solution3.set_color_by_tex("v",BLUE)

        x_component_solution4 = MathTex("{x}(t)","=","v_{i,x}","t").move_to(x_component_solution3)
        x_component_solution4.set_color_by_tex("v",BLUE)

        x_component_solution5 = MathTex("{x}(t)","=","v_i",r"\cos(\theta)","t").move_to(x_component_solution4)
        x_component_solution5.set_color_by_tex("v",BLUE)


        sine_ratio = MathTex(r"\sin(\theta)","=","{o",r"\over","h}","=",r"{v_{i,y}",r"\over",r"v_i}").to_edge(UR)
        sine_ratio.set_color_by_tex("{o",PURPLE)
        sine_ratio.set_color_by_tex("h}",BLUE)
        sine_ratio.set_color_by_tex("v_i",BLUE)
        sine_ratio.set_color_by_tex("v_{i,y}",PURPLE)

        y_velocity_equation = MathTex("v_{i,y}","=","v_i",r"\sin(\theta)").next_to(sine_ratio,DOWN)
        y_velocity_equation.set_color_by_tex("v_{i,y}",PURPLE)
        y_velocity_equation.set_color_by_tex("v_i",BLUE)

        y_component_solution1 = MathTex("{y}(t)","=","{y}_i","+","v_{i,y}","t","+",r"\frac{1}{2}","{a}_y","t","^2").next_to(y_velocity_equation,DOWN).shift(0.5*RIGHT).to_edge(RIGHT)
        y_component_solution1.set_color_by_tex("v",BLUE)

        y_component_solution2 = MathTex("{y}(t)","=","0","+","v_{i,y}","t","+",r"\frac{1}{2}","{a}_y","t","^2").move_to(y_component_solution1).to_edge(RIGHT)
        y_component_solution2.set_color_by_tex("v",BLUE)

        y_component_solution3 = MathTex("{y}(t)","=","v_{i,y}","t","-",r"\frac{1}{2}","{g}","t","^2").move_to(y_component_solution2).to_edge(RIGHT)
        y_component_solution3.set_color_by_tex("v",BLUE)
        
        y_component_solution4 = MathTex("{y}(t)","=","v_i",r"\sin(\theta)","t","-",r"\frac{1}{2}","{g}","t","^2").move_to(y_component_solution3).to_edge(RIGHT)
        y_component_solution4.set_color_by_tex("v",BLUE)

        set_math_colors(x_component_solution1,x_component_solution2,x_component_solution3,x_component_solution4,x_component_solution5,
                        y_component_solution1,y_component_solution2,y_component_solution3,y_component_solution4)
        
        initial_velocity_cpy = initial_velocity.copy()

        right_equation_brace = Brace(y_component_solution4,DOWN)
        left_equation_brace = Brace(x_component_solution5,DOWN)

        example_scene_mobjects = VGroup(dots,cannon,dotted_line,theta,angle,background_lines,initial_velocity,
                                        initial_velocity_cpy,velocity_y_component,initial_velocity_label,velocity_x_label,
                                        velocity_y_label)

        self.play(Write(wheel),Write(barrel))
        self.play(barrel.animate.rotate(PI/6,about_point=wheel.get_center()))
        self.play(FadeIn(background_lines),Write(angle),FadeIn(theta),Write(dots),Write(dotted_line),run_time=1.5,rate_func=rate_functions.smooth)
        self.wait()
        self.play(cannon.animate.fade(0.5),dots.animate.set_opacity(0.5),dotted_line.animate.set_opacity(0.5),angle.animate.fade(0.5),
                  FadeIn(initial_velocity_label),GrowArrow(initial_velocity))


        self.play(Transform(initial_velocity_cpy,velocity_x_component),GrowArrow(velocity_y_component),theta.animate.shift(0.2*LEFT),
                    FadeIn(velocity_x_label,velocity_y_label))
        self.wait()
        self.play(Transform(VGroup(theta,angle,initial_velocity,velocity_x_component,velocity_y_component).copy(),cosine_ratio))
        self.wait()
        self.play(FadeIn(x_velocity_equation))
        self.wait()
        self.play(example_scene_mobjects.animate.shift(0.75*DOWN),Write(x_component_solution1))
        self.wait()
        self.play(Transform(x_component_solution1,x_component_solution2))
        self.wait()
        self.play(Transform(x_component_solution1,x_component_solution3))
        self.wait()
        self.play(Transform(x_component_solution1,x_component_solution4))
        self.wait()
        self.play(Transform(x_component_solution1,x_component_solution5))
        self.wait()
        self.play(Transform(VGroup(theta,angle,initial_velocity,velocity_x_component,velocity_y_component).copy(),sine_ratio))
        self.wait()
        self.play(FadeIn(y_velocity_equation))
        self.wait()
        self.play(Write(y_component_solution1),FadeOut(dots),example_scene_mobjects[1:].animate.shift(2.5*RIGHT))
        self.wait()
        self.play(Transform(y_component_solution1,y_component_solution2))
        self.wait()
        self.play(Transform(y_component_solution1,y_component_solution3))
        self.wait()
        self.play(Transform(y_component_solution1,y_component_solution4))
        self.wait()
        self.play(Write(right_equation_brace))
        self.wait()
        self.play(Write(left_equation_brace))
        self.wait()
        self.play(FadeOut(left_equation_brace,right_equation_brace))        
        self.wait()

class CircularMotion(Scene):
    def construct(self):
        circle_radius = 3

        circle_creation_angle = ValueTracker(-0.001)
        circle_angle = ValueTracker(0)
        theta_def_angle = ValueTracker(0)

        circle_origin = Dot(ORIGIN)

        circle_arc = always_redraw(lambda: Arc(radius=circle_radius,start_angle=0,angle=circle_creation_angle.get_value(),color=WHITE).move_arc_center_to(circle_origin.get_center())) 
        circle_square = Square(fill_color=WHITE,fill_opacity=0.5).scale(0.5).add_updater(lambda mob: mob.move_to(circle_arc.get_end()))
        
        circle_radius_line = Line(start=LEFT,end=RIGHT,color=WHITE).add_updater(lambda mob: mob.put_start_and_end_on(circle_origin.get_center(),circle_origin.get_center()+circle_radius*np.cos(circle_angle.get_value())*RIGHT+circle_radius*np.sin(circle_angle.get_value())*UP))
        circle_angle_arc = always_redraw(lambda: Arc(radius=circle_radius/2,start_angle=0,angle=circle_angle.get_value()).move_arc_center_to(circle_origin.get_center()))

        vertical_dotted = DashedLine(start=(circle_radius+0.5)*LEFT,end=(circle_radius+0.5)*RIGHT)
        horizontal_dotted = DashedLine(start=(circle_radius+0.5)*DOWN,end=(circle_radius+0.5)*UP)

        theta = Tex(r"$\theta$").move_to(1.75*RIGHT+0.75*UP)

        omega_definition = MathTex(r"\omega","=",r"{\Delta \theta",r"\over",r"\Delta t}").to_edge(UL).shift(RIGHT)
        angle_from_omega = MathTex(r"\theta","=",r"\omega","t").next_to(omega_definition,DOWN)

        set_math_colors(omega_definition,angle_from_omega)

        theta_definition_arc = always_redraw(lambda: Arc(radius=circle_radius,start_angle=0,angle=theta_def_angle.get_value(),color=BLUE).set_z_index(11).move_arc_center_to(circle_origin.get_center()))

        r_vector = Vector(color=RED).set_z_index(11).add_updater(lambda mob: mob.put_start_and_end_on(circle_origin.get_center(),circle_origin.get_center()+circle_radius*np.cos(circle_angle.get_value())*RIGHT+circle_radius*np.sin(circle_angle.get_value())*UP))
        r_label = Tex(r"$\vec{r}$",color=RED).set_z_index(11).add_updater(lambda mob: mob.next_to(r_vector.get_end(),UP))

        v_vector = Vector(color=BLUE).set_z_index(12).add_updater(lambda mob: mob.put_start_and_end_on(circle_origin.get_center()+circle_radius*np.cos(circle_angle.get_value())*RIGHT+circle_radius*np.sin(circle_angle.get_value())*UP,
                                                                                                      circle_origin.get_center()+circle_radius*np.cos(circle_angle.get_value())*RIGHT+circle_radius*np.sin(circle_angle.get_value())*UP -
                                                                                                      (circle_radius/2)*np.sin(circle_angle.get_value())*RIGHT + (circle_radius/2)*np.cos(circle_angle.get_value())*UP))
        v_label = Tex(r"$\vec{v}$",color=BLUE).set_z_index(12).add_updater(lambda mob: mob.next_to(v_vector.get_end(),UP))

        a_vector = Vector(color=GREEN).set_z_index(13).add_updater(lambda mob: mob.put_start_and_end_on(circle_origin.get_center()+circle_radius*np.cos(circle_angle.get_value())*RIGHT+circle_radius*np.sin(circle_angle.get_value())*UP,
                                                                                                        circle_origin.get_center()+0.25*circle_radius*np.cos(circle_angle.get_value())*RIGHT+0.25*circle_radius*np.sin(circle_angle.get_value())*UP))
        a_label = Tex(r"$\vec{a}$",color=GREEN).set_z_index(13).add_updater(lambda mob: mob.next_to(a_vector.get_end(),UL).shift(0.25*RIGHT))

        self.play(Write(circle_square))
        self.add(circle_arc)
        self.play(circle_creation_angle.animate.set_value(2*PI),
                    Write(vertical_dotted),Write(horizontal_dotted),Write(circle_origin),rate_func=rate_functions.ease_in_out_cubic,run_time=2)
        self.play(Uncreate(circle_square),Write(circle_radius_line))
        self.add(circle_angle_arc)
        self.play(circle_angle.animate.set_value(PI/4),Write(theta))
        self.wait()
        self.play(VGroup(horizontal_dotted,vertical_dotted,theta,circle_origin).animate.shift(2.5*RIGHT),
                    Write(omega_definition))
        self.wait()
        self.play(Write(angle_from_omega))
        self.wait()

        theta_radius = Line(start=circle_origin.get_center(),end=circle_origin.get_center()+circle_radius*RIGHT,color=BLUE_C)
        radius_label = Tex("$r$",color=RED).move_to(circle_origin.get_center() + 0.5*DOWN + 1.5*RIGHT)
        arc_length_label = Tex(r"$s$",color=RED).move_to(circle_origin.get_center()+3*RIGHT+1.5*UP)

        theta_length_def = MathTex(r"\theta","=","{{s}",r"\over","{r}}").next_to(angle_from_omega,DOWN).shift(0.5*DOWN)
        omega_from_velocity = MathTex(r"\omega","=",r"{\Delta \theta",r"\over",r"\Delta t}","=","{1",r"\over","r}",r"{\Delta {s}",r"\over",r"\Delta t}").next_to(theta_length_def,DOWN)
        omega_from_velocity2 = MathTex(r"\omega","=","{{v}",r"\over","{r}}").next_to(theta_length_def,DOWN)

        pos_vec_eqn = MathTex(r"\vec{r}","=","\ ","<","{r}",r"\cos(\theta)",",","{r}",r"\sin(\theta)",">").next_to(omega_from_velocity2,DOWN).shift(0.5*DOWN).to_edge(LEFT)
        pos_vec_eqn2 = MathTex(r"\vec{r}","=","\ ","<","{r}",r"\cos(",r"\omega","t",")",",","{r}",r"\sin(",r"\omega","t",")",">").next_to(omega_from_velocity2,DOWN).shift(0.5*DOWN).to_edge(LEFT)

        velocity_vec_eqn = MathTex(r"\vec{v}","=",r"{d",r"\vec{r}",r"\over","d","t}").next_to(pos_vec_eqn,DOWN).to_edge(LEFT)
        velocity_vec_eqn2 = MathTex(r"\vec{v}","=","\ ","<","-","{r}",r"\omega",r"\sin(",r"\omega","t",")",",","{r}",r"\omega",r"\cos(",r"\omega","t",")",">").next_to(pos_vec_eqn,DOWN).to_edge(LEFT)

        acceleration_vec_eqn = MathTex(r"\vec{a}","=","r{d",r"\vec{v}",r"\over","d","t}").scale(0.75).next_to(velocity_vec_eqn2,DOWN).to_edge(LEFT)
        acceleration_vec_eqn2 = MathTex(r"\vec{a}","=","\ ","<","-","{r}",r"\omega","^2",r"\cos(",r"\omega","t",")",",","-","{r}",r"\omega","^2",r"\sin(",r"\omega","t",")",">").next_to(velocity_vec_eqn2,DOWN).to_edge(LEFT)
        acceleration_vec_eqn3 = MathTex(r"\vec{a}","=","\ ","<","-","{r}",r"\omega","^2",r"\cos(",r"\omega","t",")",",","-","{r}",r"\omega","^2",r"\sin(",r"\omega","t",")",">","\ ","=","-",r"\omega","^2",r"\vec{r}").next_to(velocity_vec_eqn2,DOWN).to_edge(LEFT)

        velocity_magnitude = MathTex(r"|\vec{v}|","=","{r}",r"\omega").next_to(omega_definition.copy().to_edge(LEFT)).shift(RIGHT)
        velocity_magnitude2 = MathTex(r"|\vec{v}|","=","{r}",r"{{v}",r"\over","{r}}").next_to(omega_definition.copy().to_edge(LEFT)).shift(RIGHT)
        velocity_magnitude3 = MathTex(r"|\vec{v}|","=","{v}").next_to(omega_definition.copy().to_edge(LEFT)).shift(RIGHT)

        acceleration_magnitude = MathTex(r"|\vec{a}|","=","{r}",r"\omega","^2").next_to(velocity_magnitude3,DOWN)
        acceleration_magnitude2 = MathTex(r"|\vec{a}|","=","{r}",r"{{v}^2",r"\over","{r}^2}").next_to(velocity_magnitude3,DOWN)
        acceleration_magnitude3 = MathTex(r"|\vec{a}|","=",r"{{v}^2",r"\over","{r}}").next_to(velocity_magnitude3,DOWN)

        set_math_colors(theta_length_def,omega_from_velocity,omega_from_velocity2,
                        pos_vec_eqn,pos_vec_eqn2,velocity_vec_eqn,velocity_vec_eqn2,
                        acceleration_vec_eqn,acceleration_vec_eqn2,acceleration_vec_eqn3,
                        velocity_magnitude,velocity_magnitude2,velocity_magnitude3,
                        acceleration_magnitude,acceleration_magnitude2,acceleration_magnitude3)
        
        self.add(theta_definition_arc)
        self.play(Write(theta_radius),theta_def_angle.animate.set_value(PI/4),FadeIn(radius_label,arc_length_label))
        self.wait()
        self.play(Write(theta_length_def))
        self.wait()
        self.play(Write(omega_from_velocity))
        self.wait()
        self.play(Transform(omega_from_velocity,omega_from_velocity2))
        self.wait()
        self.play(Write(pos_vec_eqn),Write(r_vector),Write(r_label))
        self.wait()
        self.play(Transform(pos_vec_eqn,pos_vec_eqn2))
        self.wait()
        self.play(Write(velocity_vec_eqn),Write(v_vector),Write(v_label))
        self.wait()
        self.play(Transform(velocity_vec_eqn,velocity_vec_eqn2))
        self.wait()
        self.play(VGroup(omega_definition,angle_from_omega,theta_length_def,omega_from_velocity).animate.to_edge(LEFT),
                  Write(velocity_magnitude))
        self.wait()
        self.play(Transform(velocity_magnitude,velocity_magnitude2))
        self.wait()
        self.play(Transform(velocity_magnitude,velocity_magnitude3))
        self.wait()
        self.play(Write(acceleration_vec_eqn),Write(a_vector),Write(a_label))
        self.wait()
        self.play(Transform(acceleration_vec_eqn,acceleration_vec_eqn2))
        self.wait()
        self.play(VGroup(horizontal_dotted,vertical_dotted,theta,circle_origin,theta_radius).animate.shift(RIGHT),
                  FadeOut(acceleration_vec_eqn),FadeIn(acceleration_vec_eqn3))
        self.wait()
        original_theta = Arc(radius=circle_radius/2,start_angle=0,angle=circle_angle.get_value()).move_arc_center_to(circle_origin.get_center())
        self.play(Write(acceleration_magnitude),circle_angle.animate.set_value(2*PI+PI/4),
                    FadeOut(circle_angle_arc),FadeIn(original_theta))
        self.wait()
        self.play(Transform(acceleration_magnitude,acceleration_magnitude2))
        self.wait(0.25)
        self.play(Transform(acceleration_magnitude,acceleration_magnitude3))
        self.wait()

class ReferenceFrames(Scene):
    def construct(self):
        header = Text("Reference Frames").scale(1.5)
        airplane = SVGMobject("img/airplane.svg")
        airplane_vector = Vector(color=BLUE_B).put_start_and_end_on(UL,UP+5*RIGHT)
        airplane_vector_label = Tex(r"$900 \frac{km}{h}$",color=BLUE_B).next_to(airplane_vector.get_end(),UR)
        airplane_velocity_group = VGroup(airplane_vector,airplane_vector_label)

        ground_vector = Vector(color=GREEN_B).put_start_and_end_on(2*DOWN+5*RIGHT,2*DOWN+LEFT).shift(RIGHT)
        ground_vector_label = Tex(r"$900 \frac{km}{h}$",color=GREEN_B).next_to(ground_vector.get_end(),UP)
        ground_velocity_group = VGroup(ground_vector,ground_vector_label)

        airplane_vector2 = Vector(color=BLUE_B).put_start_and_end_on(UL,UP+4*RIGHT)
        airplane_vector_label2 = Tex(r"$900 \frac{km}{h}$",color=BLUE_B).next_to(airplane_vector2.get_end(),UP)
        airplane_velocity_group2 = VGroup(airplane_vector2,airplane_vector_label2)

        ground = Line(start=3*DOWN+7*LEFT,end=3*DOWN+7*RIGHT,color=GREEN)
        stick_man = SVGMobject("img/stick-man.svg").shift(2*DL)

        car = SVGMobject("img/car-side-view.svg").shift(2*DOWN+2*LEFT)

        car_vector = Vector(color=RED_B).put_start_and_end_on(2*DOWN+5*LEFT,2*DOWN+5.56*LEFT)
        car_vector_label = Tex(r"$100 \frac{km}{h}$",color=RED_B).next_to(car_vector.get_end(),UP)
        car_vector_group = VGroup(car_vector,car_vector_label)

        ground_from_car_vector = Vector(color=GREEN).put_start_and_end_on(2.5*DOWN+2*RIGHT,2.5*DOWN+3*RIGHT)
        ground_from_car_vector_label = Tex(r"$100 \frac{km}{h}$",color=GREEN).next_to(ground_from_car_vector.get_end(),UP)
        ground_from_car_group = VGroup(ground_from_car_vector,ground_from_car_vector_label)

        plane_from_car_vector = Vector(color=BLUE_B).put_start_and_end_on(4*RIGHT+UP,4.56*RIGHT+UP)
        plane_from_car_vector_label = Tex(r"$100 \frac{km}{h}$",color=BLUE_B).next_to(plane_from_car_vector,DR)
        plane_from_car_vector_group = VGroup(plane_from_car_vector,plane_from_car_vector_label)

        thousand_kph = Tex(r"$1000 \frac{km}{h}$",color=BLUE_B).next_to(plane_from_car_vector,RIGHT)

        self.play(Write(header))
        self.wait()
        self.play(header.animate.to_edge(UP))
        self.wait()
        self.play(Write(airplane))
        self.play(airplane.animate.shift(UP+3*LEFT))
        self.wait()
        self.play(GrowArrow(airplane_vector),FadeIn(airplane_vector_label))
        self.wait()
        self.play(Write(ground),Write(stick_man))
        self.wait()
        self.play(Transform(airplane_velocity_group,ground_velocity_group))
        self.wait()
        self.play(Transform(airplane_velocity_group,airplane_velocity_group2),stick_man.animate.shift(7*RIGHT))
        self.wait()
        self.play(Write(car),Write(car_vector_group))
        self.wait()
        self.play(Transform(car_vector_group,ground_from_car_group),Write(plane_from_car_vector_group))
        self.wait()
        self.play(Transform(VGroup(plane_from_car_vector_label,airplane_vector_label),thousand_kph))
        self.wait()

class EarthAroundSun(Scene):
    def construct(self):
        orbit_angle = ValueTracker(0)
        orbit_radius = 4

        earth = SVGMobject("img/earth.svg").add_updater(lambda mob: mob.move_to(orbit_radius*np.cos(orbit_angle.get_value())*RIGHT+
                                                                                orbit_radius*np.sin(orbit_angle.get_value())*UP))
        sun = ImageMobject("img/sun.png").scale(0.33)

        self.play(Write(earth),FadeIn(sun))
        self.play(orbit_angle.animate.set_value(2*PI))
        self.wait()

class SolarSystemAroundGalaxy(Scene):
    def construct(self):
        orbit_angle = ValueTracker(PI/4)
        orbit_radius = 4

        milky_way = ImageMobject("img/milky-way.jpg").scale(0.1)
        sun = ImageMobject("img/sun.png").scale(0.1).add_updater(lambda mob: mob.move_to(orbit_radius*np.cos(orbit_angle.get_value())*RIGHT+
                                                                                    orbit_radius*np.sin(orbit_angle.get_value())*UP))

        self.play(FadeIn(milky_way),FadeIn(sun))
        self.play(orbit_angle.animate.set_value(2*PI+PI/4))
        self.wait()

