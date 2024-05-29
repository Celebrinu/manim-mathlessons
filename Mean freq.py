from manim import *
#config.disable_caching = True

class BarChartWithoutAxes(BarChart):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.remove(self.x_axis, self.y_axis)  # Remove axes when creating the object


class StatMEANfreq(Scene):
    def construct(self):
                #self.wait(3)
        grid = NumberPlane()
        array00= np.array([4, 4, 2, 2, 2, 2, 2, 6])
        array0 = np.array([4, 2, 6])
        array0mean = np.array([3, 3, 3])
        array11 = np.array([4, 2, 6, 10, 4, 6, 5, 3, 9, 1])
        array1 = np.array([4, 2, 6, 10, 4, 6, 5, 3, 1])
        array1mean = np.array([4, 4, 4, 4, 4, 4, 4, 4, 4])
        

        formula= MathTex(r"\text{Medelvärde}=\frac{\text{Summa av alla värden}}{\text{Antal värden}}").shift([0, 2.5, 0])
        formula0= MathTex(r"\frac{4\cdot 2+2\cdot 5+6}{2+5+1}=\frac{24}{8}").shift([-2.5, 2.5, 0])
        formula1 = MathTex(r"\frac{4\cdot \:4\:+\:7\cdot \:5\:+\:3\cdot \:6\:+4\cdot \:6\:+\:6\cdot \:12\:+\:5\cdot \:2\:+\:3\cdot \:6\:+\:3\cdot \:5\:+\:1\cdot \:8}{4\:+\:5\:+\:6\:+\:6\:+\:12\:+\:2\:+\:6\:+\:5\:+\:8}").shift([0, 2.8, 0]).scale(0.8)


        formula1ans= MathTex(r"=3").next_to(formula0)  #,DOWN)

        
        
        chart0 = BarChartWithoutAxes(values=array00,
                          y_range=[0, 13, 1],
                          x_axis_config = {'color':YELLOW},
                          y_axis_config = {'color':BLACK , 'font_size': 1})
        
        c0_bar_lbls = chart0.get_bar_labels(
            color=WHITE, label_constructor=MathTex, font_size=36
        )


        chart1 = BarChartWithoutAxes(values=array0,
                          y_range=[0, 13, 1],
                          x_axis_config = {'color':BLACK},
                          y_axis_config = {'color':BLACK , 'font_size': 1})

        c_bar_lbls = chart1.get_bar_labels(
            color=WHITE, label_constructor=MathTex, font_size=36
        )

                # Freq numbering
        freq_numbers = VGroup(
            MathTex("2").next_to(chart1.bars[0], DOWN),
            MathTex("5").next_to(chart1.bars[1], DOWN),
            MathTex("1").next_to(chart1.bars[2], DOWN)
        )
        
        self.wait()

        amean0=np.mean(array00)
        amean1=np.mean(array1mean)
        amean_tex = MathTex(f"\\text{{Medelvärde}} = {amean0:.2f}").next_to(formula0, buff=0.5)  # Format the mean value to two decimal places

        self.remove(chart0.x_axis,chart0.y_axis)
        self.play(FadeIn(chart0, c0_bar_lbls))
        
        self.wait(2)
        self.remove(chart1.x_axis,chart1.y_axis)

        self.play(ReplacementTransform(chart0.bars[0:2],chart1.bars[0]),ReplacementTransform(chart0.bars[2:7],chart1.bars[1]),ReplacementTransform(chart0.bars[7],chart1.bars[2]),ReplacementTransform(c0_bar_lbls,c_bar_lbls),FadeIn(chart1))  
        self.remove(chart0)
        self.play(FadeIn(freq_numbers))
        self.wait()
        self.play(Write(formula))
        self.wait(2)
        self.play(FadeOut(formula))
        self.wait()
        self.play(Write(formula0))
        self.wait()
        self.play(Write(amean_tex))
        
        self.wait()

        
        chart1.generate_target()
        c_bar_lbls.generate_target()

        chart1.target.change_bar_values(array0mean)
        c_bar_lbls.target = chart1.target.get_bar_labels(color=WHITE, font_size=36)

        self.play(MoveToTarget(chart1),MoveToTarget(c_bar_lbls))

        self.wait(5)
        self.play(FadeOut(chart1, c_bar_lbls, formula0, amean_tex, freq_numbers)) #fade and wait for example 2

        self.wait(2)
        chart1 = BarChart(values=array1,
                          y_range=[0, 13, 1],
                          x_axis_config = {'color':BLACK},
                          y_axis_config = {'color':BLACK , 'font_size': 1})

        c_bar_lbls = chart1.get_bar_labels(
            color=WHITE, label_constructor=MathTex, font_size=36
        )

                # Freq numbering2
        freq_numbers = VGroup(
            MathTex("4").next_to(chart1.bars[0], DOWN),
            MathTex("7").next_to(chart1.bars[1], DOWN),
            MathTex("3").next_to(chart1.bars[2], DOWN),
            MathTex("1").next_to(chart1.bars[3], DOWN),
            MathTex("6").next_to(chart1.bars[4], DOWN),
            MathTex("12").next_to(chart1.bars[5], DOWN),
            MathTex("2").next_to(chart1.bars[6], DOWN),
            MathTex("11").next_to(chart1.bars[7], DOWN),
            MathTex("8").next_to(chart1.bars[8], DOWN),
        )

        self.wait()
        self.play(FadeIn(chart1, c_bar_lbls, freq_numbers)) #print chart scene 2
        self.wait(2)
        amean_tex = MathTex(f"\\text{{Medelvärde}} = {amean1:.2f}").shift(2.9,-1.2,0)  # Format the mean value to two decimal places
        self.play(Write(formula1))
        self.wait()
        formula11= MathTex(r"=\frac{216}{54}").next_to(amean_tex, LEFT*7)
        self.play(Write(formula11))
        self.wait()
        self.play(Write(amean_tex))
        self.wait(5)

        

        chart1.generate_target()
        c_bar_lbls.generate_target()

        chart1.target.change_bar_values(array1mean)
        c_bar_lbls.target = chart1.target.get_bar_labels(color=WHITE, font_size=36)

        self.play(MoveToTarget(chart1),MoveToTarget(c_bar_lbls))
        self.wait(3)
        #self.play(FadeOut(chart1, c_bar_lbls, formula1, amean_tex)) #fade and wait for next scene
        self.wait(2)