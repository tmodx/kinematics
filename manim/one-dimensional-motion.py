from manim import *
import numpy as np

def set_math_colors(*equations):
    for equation in equations:
        equation.set_color_by_tex("{x}",RED)
        equation.set_color_by_tex("{y}",RED)
        equation.set_color_by_tex("{v}",BLUE)
        equation.set_color_by_tex("{a}",GREEN)

class OneDimensionPositionDisplacementVelocity(Scene):
    def construct(self):
        # grid = NumberPlane()
        ax = NumberLine(length=14,include_tip=True).set_opacity(0.95)
        ax2 = NumberLine(length=14,include_tip=True,include_numbers=True).set_opacity(0.95)
        ax2.numbers[7].set_color(RED)
        ax2.numbers[9].set_color(RED)
        ax_labels = Tex("$x$").next_to(ax.get_tip(),UP)


        position_tracker = ValueTracker(0)

        system = Square(side_length=1.5,fill_color=BLACK,fill_opacity=0.75)
        system.add_updater(lambda mob: mob.move_to(RIGHT*position_tracker.get_value()))

        system_position_label = DecimalNumber()
        system_position_label.add_updater(lambda mob: mob.set_value(position_tracker.get_value()).next_to(system,UP))

        dot = Dot(color=WHITE).set_z_index(5).add_updater(lambda mob: mob.move_to(system))

        EPSILON = 1e-6
        movement_vec = Vector(color=RED).set_z_index(10).add_updater(lambda mob: mob.put_start_and_end_on(ORIGIN,dot.get_center()+EPSILON*RIGHT))

        delta_x = MathTex(r"\text{Displacement: }",r"\Delta {x}","=","{2}","-","0","=","2").to_corner(UL).shift(RIGHT)
        delta_x.set_color_by_tex("2",RED)
        delta_x.set_color_by_tex("0",RED)

        delta_x2 = MathTex(r"\text{Displacement: }",r"\Delta {x}","=","{x}_f","-","{x}_i").shift(2*UP)

        ax2_red_numbers = VGroup(ax2.numbers[7],ax2.numbers[9]).copy()

        velocity1 = MathTex(r"{\Delta {x}",r"\over",r"\Delta t}").next_to(delta_x2,DOWN)
        velocity2 = MathTex(r"\text{Velocity: }",r"{\Delta {x}",r"\over",r"\Delta t}").next_to(delta_x2,DOWN)

        velocity3_example = MathTex(r"\text{Velocity: }",r"{\Delta {x}",r"\over",r"\Delta t}","=","{5m",r"\over","2s}","=",r"2.5 \frac{m}{s}").next_to(delta_x2,DOWN)
        velocity3_example.set_color_by_tex("5m",RED)
        velocity3_example.set_color_by_tex("2.5",BLUE)

        velocity4 = MathTex(r"\text{Velocity: }",r"\displaystyle \lim_{\Delta t \to 0}" ,r"{\Delta {x}",r"\over",r"\Delta t}","=","{5m",r"\over","2s}","=",r"2.5 \frac{m}{s}").next_to(delta_x2,DOWN)
        velocity4.set_color_by_tex("5m",RED)
        velocity4.set_color_by_tex("2.5",BLUE)

        velocity5 = MathTex(r"\text{Velocity: }",r"\displaystyle \lim_{\Delta t \to 0}" ,r"{\Delta {x}",r"\over",r"\Delta t}").next_to(delta_x2,DOWN)

        set_math_colors(delta_x,delta_x2,velocity1,velocity2,velocity3_example,velocity4,velocity5)

        # self.add(grid)
        self.play(Write(ax),Write(system),lag_ratio=0.5)
        self.play(position_tracker.animate.set_value(1),rate_func=rate_functions.smooth)
        self.play(position_tracker.animate.set_value(-1),rate_func=rate_functions.smooth)
        self.play(position_tracker.animate.set_value(0),rate_func=rate_functions.smooth)
        self.wait()
        self.play(Write(ax_labels),FadeIn(system_position_label))
        self.wait()
        self.play(position_tracker.animate.set_value(2),rate_func=rate_functions.smooth)
        self.play(position_tracker.animate.set_value(-2),rate_func=rate_functions.smooth)
        self.play(position_tracker.animate.set_value(0),rate_func=rate_functions.smooth)
        self.wait()
        self.play(Write(dot))
        self.play(Write(movement_vec))
        self.play(position_tracker.animate.set_value(2),rate_func=rate_functions.smooth)
        self.wait()
        self.play(Write(ax2.numbers[1:]))
        self.wait()
        self.play(Transform(ax2_red_numbers,delta_x))
        self.wait(2)
        self.play(FadeOut(ax,ax2.numbers[1:],system,dot,movement_vec,ax_labels,system_position_label),Transform(ax2_red_numbers,delta_x2))
        self.wait() 
        self.play(Write(velocity1))
        self.wait() 
        self.play(Transform(velocity1,velocity2))
        self.wait() 
        self.play(Transform(velocity1,velocity3_example))
        self.wait() 
        self.play(Transform(velocity1,velocity4))
        self.wait() 
        self.play(Transform(velocity1,velocity5))
        self.wait() 

class PositionVelocityAccelerationGraphs(Scene):
    def construct(self):
        # I made these in desmos first
        position_graph = FunctionGraph(lambda t: np.sin(t) + 3 - 0.02 * t**2)
        velocity_graph = FunctionGraph(lambda t: np.cos(t) - 0.02*2*t)

        position_axes = Axes(
            x_range = [0,10,1],
            y_range = [0,5,1],
            tips=False,
        ).stretch(0.5,1).stretch(0.75,0).to_edge(UP)

        velocity_axes = Axes(
            x_range = [0,10,1],
            y_range = [-2,2,1],
            tips=False,
        ).stretch(0.5,1).stretch(0.75,0).to_edge(UP).to_edge(DOWN)

        acceleration_axes = velocity_axes.copy()

        position_labels = position_axes.get_axis_labels(x_label=Tex("$t$"),y_label=Tex("$x$",color=RED))
        velocity_labels = velocity_axes.get_axis_labels(x_label=Tex("$t$"),y_label=Tex("$v$",color=BLUE))
        acceleration_labels = acceleration_axes.get_axis_labels(x_label=Tex("$t$"),y_label=Tex("$a$",color=GREEN))

        position_graph_length = ValueTracker(0)
        acceleration_graph_length = ValueTracker(0)
        t = ValueTracker(0)
        delta_t = 1e-6

        position_graph = always_redraw(
            lambda: position_axes.plot(lambda t: np.sin(t) + 3 - 0.02 * t**2,color=RED,
                                        x_range=[0,position_graph_length.get_value()]))

        velocity_graph = always_redraw(
            lambda: velocity_axes.plot(lambda t: np.cos(t) - 0.02*2*t,color=BLUE,
                                     x_range=[0,t.get_value()]) )
        
        acceleration_graph = always_redraw(
            lambda: acceleration_axes.plot(lambda t: -np.sin(t) - 0.02*2,color=GREEN,
                                            x_range=[0,acceleration_graph_length.get_value()])
        )

        tangent = always_redraw(
            lambda: position_axes.get_secant_slope_group(
                x=t.get_value(),
                graph=position_graph,
                dx=delta_t,
                dx_line_color=WHITE,
                dy_line_color=WHITE,
                secant_line_color=BLUE,
                secant_line_length=4
            )
        )

        tangent_dot = always_redraw(
            lambda: Dot(color=GREEN).set_z_index(5).move_to(position_axes.c2p(t.get_value(),position_graph.underlying_function(t.get_value())))
        )

        self.play(Write(position_axes),Write(position_labels),Write(velocity_axes),Write(velocity_labels))
        self.wait()
        self.add(position_graph)
        self.play(position_graph_length.animate.set_value(10),rate_func=rate_functions.smooth,run_time=2)
        self.wait()
        self.play(Write(tangent),Write(tangent_dot))
        self.add(velocity_graph)
        self.play(t.animate.set_value(10),Write(velocity_graph),rate_func=rate_functions.smooth,run_time=2)
        self.play(FadeOut(tangent,tangent_dot))
        self.wait()
        self.play(VGroup(velocity_axes,velocity_labels).animate.next_to(VGroup(position_axes,position_labels),DOWN))

        VGroup(acceleration_axes,acceleration_labels).next_to(VGroup(velocity_axes,velocity_labels),DOWN)

        self.play(FadeIn(acceleration_axes,acceleration_labels,acceleration_graph))
        self.play(AnimationGroup(VGroup(position_axes,position_graph,position_labels,
                         velocity_axes,velocity_graph,velocity_labels,
                         acceleration_axes,acceleration_labels).animate.scale(2/3).to_edge(UP),
                         acceleration_graph_length.animate.set_value(10),lag_ratio=0.35,rate_func=rate_functions.smooth,run_time=2))
        self.wait()

class Acceleration(Scene):
    def construct(self):
        header = Text("Acceleration").scale(1.5).to_edge(UP).shift(0.5*DOWN)
        acceleration_eqn = MathTex("{a}","=",r"{\Delta {v}",r"\over",r"\Delta t}")
        acceleration_eqn2 = MathTex("{a}","=",r"\displaystyle \lim_{\Delta t \to 0}",r"{\Delta {v}",r"\over",r"\Delta t}").scale(1.5)
        set_math_colors(acceleration_eqn,acceleration_eqn2)

        self.play(Write(header))
        self.wait()
        self.play(Write(acceleration_eqn))
        self.play(acceleration_eqn.animate.scale(1.5))
        self.wait()
        self.play(Transform(acceleration_eqn,acceleration_eqn2))
        self.wait()

class ConstantVelocityEquations(Scene):
    def construct(self):
        average_velocity = MathTex(r"{v}_{\text{avg}}","=",r"{ \Delta {x}",r"\over",r"\Delta t}")
        average_velocity2 = MathTex(r"{v}_{\text{avg}}","=",r"{{x}", "-", "{x}_i",r"\over","t - t_i}")
        average_velocity_zeroed = MathTex(r"{v}_{\text{avg}}","=",r"{{x}", "-", "{x}_i",r"\over","t - 0}").to_edge(UP)
        average_velocity_simplified = MathTex(r"{v}_{\text{avg}}","=",r"{{x}", "-", "{x}_i",r"\over","t}").to_edge(UP)

        ax = NumberLine(length=40,include_tip=True,include_numbers=True,x_range=[-20,20]).set_opacity(0.95)
        center_square = Square().shift(DOWN)
        time_brace = Brace(center_square,UP)
        delta_t_label = MathTex(r"\Delta t").next_to(time_brace,UP)

        set_math_colors(average_velocity,average_velocity2,average_velocity_zeroed,average_velocity_simplified)

        self.play(Write(average_velocity))
        self.wait()
        self.play(Transform(average_velocity,average_velocity2))
        self.wait()
        self.play(average_velocity.animate.to_edge(UP))
        self.wait()
        self.play(FadeIn(ax),Write(time_brace),Write(delta_t_label),rate_func=rate_functions.smooth,run_time=2)
        self.play(ax.animate.shift(10.4*LEFT),rate_func=rate_functions.smooth,run_time=2)
        self.play(ax.animate.shift(12*RIGHT),rate_func=rate_functions.smooth,run_time=2)
        self.play(ax.animate.shift(2.6*LEFT),rate_func=rate_functions.smooth,run_time=2)
        self.wait()
        self.play(Transform(average_velocity,average_velocity_zeroed))
        self.play(Transform(average_velocity,average_velocity_simplified))
        self.wait()

        average_velocity_solve2 = MathTex(r"{v}_{\text{avg}}","t","=",r"{{x}", "-", "{x}_i").next_to(average_velocity_simplified,DOWN)
        average_velocity_solve3 = MathTex("{x}(t)","=","{x}_i","+",r"{v}_{\text{avg}}","t").next_to(average_velocity_solve2,DOWN).shift(DOWN)
        average_acc_solve = MathTex("{v}(t)","=","{v}_i","+",r"{a}_{\text{avg}}","t").next_to(average_velocity_solve3,DOWN)
        set_math_colors(average_velocity_solve2,average_velocity_solve3,average_acc_solve)

        self.play(Write(average_velocity_solve2))
        self.wait()
        self.play(VGroup(ax,time_brace,delta_t_label).animate.shift(2*DOWN), Write(average_velocity_solve3),rate_func=rate_functions.smooth)
        self.wait()
        self.play(VGroup(ax,time_brace,delta_t_label).animate.to_edge(DOWN), Write(average_acc_solve),rate_func=rate_functions.smooth)
        self.wait(2)

class DerivativeIntegralGrid(Scene):
    def construct(self):
        # self.add(NumberPlane())
        velocity_slope = MathTex(r"{ \Delta {x}", r"\over", r"\Delta t}", "=", r"{v}_{\text{avg}}").scale(1.5).shift(3.5*LEFT+2*UP)
        acceleration_slope = MathTex(r"{ \Delta {v}", r"\over", r"\Delta t}", "=", r"{a}_{\text{avg}}").scale(1.5).shift(3.5*LEFT+2*DOWN)

        position_integral = MathTex(r"\Delta {x}","=",r"{v}_{\text{avg}}",r"\Delta t").scale(1.5).shift(3.5*RIGHT+2*UP)
        velocity_integral = MathTex(r"\Delta {v}","=",r"{a}_{\text{avg}}",r"\Delta t").scale(1.5).shift(3.5*RIGHT+2*DOWN)

        # i.e. the line is vertical / horizontal
        vertical_separator = DashedLine(start=6*UP,end=6*DOWN)
        horizontal_separator = DashedLine(start=7*LEFT,end=7*RIGHT)

        set_math_colors(velocity_slope,acceleration_slope,position_integral,velocity_integral)

        self.play(Write(velocity_slope))
        self.wait()
        self.play(Write(acceleration_slope),Write(vertical_separator),lag_ratio=0.4)
        self.play(Write(position_integral),Write(horizontal_separator),lag_ratio=0.4)
        self.play(Write(velocity_integral))
        self.wait()

class ConstantAccelerationEquations(Scene):
    def construct(self):
        let_statement = MathTex(r"Let \ ","{a}(t)","=","{a}",r"\text{ (let }", "{a}", r"\text{ be constant):}").to_edge(UP).shift(1.5*DOWN)
        velocity_riemann = MathTex("{v}(t)","=",r"\displaystyle \lim_{\Delta {t} \to 0}",r"\sum_{i=1}^n","{a}",r"\Delta t").next_to(let_statement,DOWN)
        velocity_riemann_integral = MathTex("{v}(t)","=",r"\int","{a}","dt").next_to(let_statement,DOWN)
        velocity_integral2 = MathTex("{v}(t)","=",r"\int","{a}","dt","=","{a}","t","+","C").next_to(let_statement,DOWN)
        velocity_integral_zeroed =  MathTex("{v}(0)","=","0","+","C").next_to(velocity_integral2,DOWN)
        velocity = MathTex("{v}(t)","=","{a}","t","+","{v}_i").next_to(velocity_integral2,DOWN)

        position_integral1 = MathTex("{x}(t)","=",r"\displaystyle \int", "{v}(t)", "dt").shift(0.5*DOWN)
        position_integral2 = MathTex("{x}(t)","=",r"\displaystyle \int", "(", "{a}", "t", "+","{v}_i",")","dt").shift(0.5*DOWN)
        position_integral3 = MathTex("{x}(t)","=",r"\displaystyle \int", "(", "{a}", "t", "+","{v}_i",")","dt","=",r"\frac{1}{2}","{a}","t^2","+","{v}_i","t","+","C").shift(0.5*DOWN)

        position_zeroed = MathTex("{x}(0)","=","0","+","0","+","C").next_to(position_integral3,DOWN)
        position = MathTex("{x}(t)","=",r"\frac{1}{2}","{a}","t^2","+","{v}_i","t","+","{x}_i").next_to(position_integral3,DOWN)

        set_math_colors(let_statement,velocity_riemann,velocity_riemann_integral,
                        velocity_integral2,velocity_integral_zeroed,velocity,
                        position_integral1,position_integral2,position_integral3,
                        position_zeroed,position)

        self.play(Write(let_statement))
        self.wait()
        self.play(Write(velocity_riemann))
        self.wait()
        self.play(Transform(velocity_riemann,velocity_riemann_integral))
        self.wait()
        self.play(Transform(velocity_riemann,velocity_integral2))
        self.wait()
        self.play(Write(velocity_integral_zeroed))
        self.wait()
        self.play(Transform(velocity_integral_zeroed,velocity))
        self.wait()
        self.play(VGroup(let_statement,velocity_riemann,velocity_integral_zeroed).animate.to_edge(UP),
                    FadeIn(position_integral1))
        self.wait()
        self.play(Transform(position_integral1,position_integral2))
        self.wait()
        self.play(Transform(position_integral1,position_integral3))
        self.wait(2)
        self.play(Write(position_zeroed))
        self.wait()
        self.play(Transform(position_zeroed,position))
        self.wait()

class Apple(Scene):
    def construct(self):
        apple = ImageMobject("img/apple.png").scale(0.25).shift(2*UP)
        scale = NumberLine(x_range=[0,1],length=3.5).rotate(PI/2).shift(LEFT)
        bg_line = Line(start=7*LEFT,end=7*RIGHT).shift(DOWN).set_opacity(0.5)
        hundred_meters_label = Tex("$100m$").next_to(scale.get_end(),LEFT)

        down_arrow = Vector(1.5*DOWN).next_to(apple,DOWN)

        t_zero = MathTex("t","=","0",":")
        v_i = MathTex("{v}_i","=","0",r"\frac{m}{s}")
        y_i = MathTex("{y}_i","=","100","m")
        acc = MathTex("{a}","=","-9.81",r"\frac{m}{s^2}")

        solution1 = MathTex("{y}(t)","=",r"\frac{1}{2}","{a}","t^2","+","{v}_i","t","+","{y}_i").to_edge(UP).shift(0.5*DOWN)
        solution2 = MathTex("0","=",r"\frac{1}{2}","{a}","t^2","+","0","t","+","{y}_i").to_edge(UP).shift(2*DOWN)
        solution3 = MathTex("0","=",r"\frac{1}{2}","{a}","t^2","+","{y}_i").to_edge(UP).shift(2*DOWN)
        solution4 = MathTex("-{y}_i","=",r"\frac{1}{2}","{a}","t^2").to_edge(UP).shift(2*DOWN)
        solution5 = MathTex("-2{y}_i","=","{a}","t^2").to_edge(UP).shift(2*DOWN)
        solution6 = MathTex("{-2{y}_i",r"\over","{a}}","=","t^2").to_edge(UP).shift(2*DOWN)
        solution7 = MathTex(r"\sqrt{","{-2{y}_i",r"\over","{a}}}","=","t").to_edge(UP).shift(2*DOWN)
        solution8 = MathTex(r"\sqrt{","{-2(100)",r"\over","-9.81}}","=","t").to_edge(UP).shift(2*DOWN)
        solution9 = MathTex("t",r"=","4.52s").to_edge(UP).shift(2.5*DOWN)

        solution_box = SurroundingRectangle(solution9,buff=0.2).set_color_by_gradient(BLUE,GREEN)

        set_math_colors(t_zero,v_i,y_i,acc,
                        solution1,solution2,solution3,solution4,solution5,solution6,solution7,solution8,solution9)
        VGroup(t_zero,v_i,y_i,acc).arrange_submobjects(DOWN).to_edge(UL).shift(0.5*DR)

        self.play(Write(bg_line),FadeIn(apple),Write(scale),Write(hundred_meters_label))
        self.wait()
        self.play(GrowArrow(down_arrow))
        self.wait(2)
        self.play(Group(apple,scale,hundred_meters_label,down_arrow).animate.to_edge(RIGHT).shift(LEFT),rate_func=rate_functions.smooth)
        self.wait()
        self.play(Write(t_zero))
        self.wait()
        self.play(Write(v_i),Write(y_i),Write(acc),run_time=2)
        self.wait()
        self.play(Write(solution1))
        self.wait()
        self.play(Write(solution2))
        self.wait()
        self.play(Transform(solution2,solution3))
        self.wait()
        self.play(Transform(solution2,solution4))
        self.wait()
        self.play(Transform(solution2,solution5))
        self.play(Transform(solution2,solution6))
        self.play(Transform(solution2,solution7))
        self.wait()
        self.play(Transform(solution2,solution8))
        self.wait()
        self.play(Transform(solution2,solution9))
        self.wait()
        self.play(Write(solution_box))
        self.play(VGroup(solution2,solution_box).animate.move_to(ORIGIN),rate_func=rate_functions.smooth)
        self.play(AnimationGroup(FadeOut(t_zero,v_i,y_i,acc,solution1,apple,down_arrow,hundred_meters_label,
                                scale,bg_line),lag_ratio=0.1),VGroup(solution2,solution_box).animate.scale(72),rate_func=rate_functions.ease_in_out_sine,run_time=2)
        self.wait()

class Cars(Scene):
    def construct(self):
        red_car = SVGMobject("img/top-down-car-red.svg").shift(1.5*UP+LEFT)
        orange_car = SVGMobject("img/top-down-car-orange.svg").shift(1.5*DOWN+RIGHT)

        red_dot = Dot(color=RED).move_to(red_car.get_center()).set_z_index(5)
        orange_dot = Dot(color=ORANGE).move_to(orange_car.get_center()).set_z_index(5)

        red_velocity = Vector(2*RIGHT,color=BLUE).put_start_and_end_on(red_dot.get_center(),red_dot.get_center()+2*RIGHT)
        orange_velocity = Vector(2*RIGHT,color=BLUE).put_start_and_end_on(orange_dot.get_center(),orange_dot.get_center()+2*RIGHT)

        red_acc = Vector(RIGHT,color=GREEN).put_start_and_end_on(red_dot.get_center(),red_dot.get_center()+RIGHT)
        orange_acc = Vector(LEFT,color=GREEN).put_start_and_end_on(orange_dot.get_center(),orange_dot.get_center()+LEFT)

        red_eqn = MathTex("x(t)","=","x_i","+","{v}_i","t","+",r"\frac{1}{2}","{a}","t^2").scale(0.67)
        red_eqn.set_color_by_tex("x",RED)
        red_eqn.next_to(red_car,UP)

        orange_eqn = MathTex("x(t)","=","x_i","+","{v}_i","t","+",r"\frac{1}{2}","{a}","t^2").scale(0.67)
        orange_eqn.set_color_by_tex("x",ORANGE)
        orange_eqn.next_to(orange_car,DOWN)

        set_math_colors(red_eqn,orange_eqn)

        dotted_line = DashedLine(start=7*LEFT,end=7*RIGHT,color=WHITE,
                                 dash_length=1.5)

        self.play(Write(red_car),Write(orange_car),Write(dotted_line),rate_func=rate_functions.smooth,run_time=2)
        self.play(Write(red_dot),Write(orange_dot),Write(red_velocity),Write(orange_velocity),
                    Write(red_acc),Write(orange_acc))
        self.play(Write(red_eqn),Write(orange_eqn))
        self.wait()

