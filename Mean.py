from manim import *
#config.disable_caching = True

#Three examples of mean with visualization in barcharts

class StatMEAN(Scene):
    def construct(self):
                #self.wait(3)
        grid = NumberPlane()

        array0 = np.array([4, 2, 6])
        array0mean = np.array([4, 4, 4])
        array1 = np.array([4, 2, 6, 10, 4, 6, 5, 3, 9, 1])
        array1mean = np.array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
        array2 = np.array([1, 2, 1, 3, 8, 9, 11, 10, 8, 7])
        array2mean = np.array([6, 6, 6, 6, 6, 6, 6, 6, 6, 6])

        formula= MathTex(r"\text{Medelvärde}=\frac{\text{Summa av alla värden}}{\text{Antal värden}}")#.shift([-2.5, 2.5, 0])
        formula0= MathTex(r"\frac{4+2+6}{3}=\frac{12}{3}").shift([-2.5, 2.5, 0])
        formula1= MathTex(r"\frac{4+2+6+10+4+6+5+3+9+1}{10}").shift([-2.5, 2.5, 0])
        formula2= MathTex(r"\frac{1+2+1+3+8+9+11+10+8+7}{10}").shift([-2.5, 2.5, 0])
        formula1ans= MathTex(r"=4").next_to(formula0)  #,DOWN)



        chart1 = BarChart(values=array0,
                          y_range=[0, 13, 1],
                          x_axis_config = {'color':BLACK},
                          y_axis_config = {'color':BLACK , 'font_size': 1})

        c_bar_lbls = chart1.get_bar_labels(
            color=WHITE, label_constructor=MathTex, font_size=36
        )

        
        self.wait()

        amean0=np.mean(array0)
        amean1=np.mean(array1)
        amean2=np.mean(array2)
        amean_tex = MathTex(f"\\text{{Medelvärde}} = {amean0:.2f}").next_to(formula0, buff=0.5)  # Format the mean value to two decimal places
        self.wait()
        self.play(Write(formula))
        self.wait(4)
        self.play(FadeOut(formula))
        self.wait()
        self.play(FadeIn(chart1, c_bar_lbls))
        self.wait(2)
        self.play(Write(formula0))
        self.wait()
        self.play(Write(amean_tex))
        
        self.wait()

        chart1.generate_target()
        c_bar_lbls.generate_target()

        chart1.target.change_bar_values(array0mean)
        c_bar_lbls.target = chart1.target.get_bar_labels(color=WHITE, font_size=36)

        self.play(MoveToTarget(chart1),MoveToTarget(c_bar_lbls))

        self.wait(3)
        self.play(FadeOut(chart1, c_bar_lbls, formula0, amean_tex)) #fade and wait for next scene
        self.wait(2)
        chart1 = BarChart(values=array1,
                          y_range=[0, 13, 1],
                          x_axis_config = {'color':BLACK},
                          y_axis_config = {'color':BLACK , 'font_size': 1})

        c_bar_lbls = chart1.get_bar_labels(
            color=WHITE, label_constructor=MathTex, font_size=36
        )


        self.wait()
        self.play(FadeIn(chart1, c_bar_lbls)) #print chart scene 2
        self.wait(2)
        amean_tex = MathTex(f"\\text{{Medelvärde}} = {amean1:.2f}").next_to(formula1, buff=0.5)  # Format the mean value to two decimal places
        self.play(Write(formula1))
        self.wait()
        self.play(Write(amean_tex))
        self.wait(5)

        chart1.generate_target()
        c_bar_lbls.generate_target()

        chart1.target.change_bar_values(array1mean)
        c_bar_lbls.target = chart1.target.get_bar_labels(color=WHITE, font_size=36)

        self.play(MoveToTarget(chart1),MoveToTarget(c_bar_lbls))
        self.wait(3)
        self.play(FadeOut(chart1, c_bar_lbls, formula1, amean_tex)) #fade and wait for next scene
        self.wait(2)

        chart1 = BarChart(values=array2,
                          y_range=[0, 13, 1],
                          x_axis_config = {'color':BLACK},
                          y_axis_config = {'color':BLACK , 'font_size': 1})

        c_bar_lbls = chart1.get_bar_labels(
            color=WHITE, label_constructor=MathTex, font_size=36
        )
        amean_tex = MathTex(f"\\text{{Medelvärde}} = {amean2:.2f}").next_to(formula1, buff=0.5)  # Format the mean value to two decimal places


        self.wait()
        self.play(FadeIn(chart1, c_bar_lbls)) #fade and wait for next scene
        self.wait(3)
        self.play(Write(formula2))
        self.wait()
        self.play(Write(amean_tex))
        self.wait(3)



        chart1.generate_target()
        c_bar_lbls.generate_target()



        chart1.target.change_bar_values(array2mean)
        c_bar_lbls.target = chart1.target.get_bar_labels(color=WHITE, font_size=36)


        self.play(MoveToTarget(chart1),MoveToTarget(c_bar_lbls))
        self.wait(3)
    