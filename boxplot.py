from manim import *
#config.disable_caching = True

class AxesWithoutY(Axes):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.remove(self.y_axis)  # Remove y-axis

class HorizontalBoxPlot(Scene):
    def construct(self):
        
        # Define data for the box plot
        data = [5, 8, 10, 12, 14, 16, 20]
        dataT = Tex(data).to_edge(UP)

        # Calculate statistics
        Min= int(np.min(data))
        Minimum= int((np.min(data))-(0.2*(np.max(data)-np.min(data))))
        Max= int(np.max(data))
        Maximum= int((np.max(data))+(0.2*(np.max(data)-np.min(data))))
        q1 = int(np.percentile(data, 25, interpolation='lower'))
        q2 = int(np.percentile(data, 50, interpolation='nearest'))
        q3 = int(np.percentile(data, 75, interpolation='higher'))

        quartilerange = q3 - q1

        #defining axes
        ax = AxesWithoutY(
            x_range=(Minimum, Maximum),
            y_range=(0, 6),
            #x_length=8,
            tips=False,
            axis_config={
            "include_numbers": True,
            "numbers_to_include": [Min, q1, q2, q3, Max],
            "numbers_with_elongated_ticks": [Min, q1, q2, q3, Max],
                        },  
                )
        
        # Add labels to the scene
        #self.add(min_label, max_label, q1_label, q2_label, q3_label)
        self.add(ax)
        self.add(dataT)

        # Calculate width and height of the polygon
        box_start = 1
        box_height = 1.5
        
        # Calculate coordinates for the polygon vertices
        vertices = [
            ax.c2p(q1, box_start),           # bottom-left corner
            ax.c2p(q3, box_start),           # bottom-right corner
            ax.c2p(q3, box_start+box_height),  # top-right corner
            ax.c2p(q1, box_start+box_height),  # top-left corner
        ]

        # Create the polygon
        box = Polygon(*vertices, color="#ffa600", fill_opacity=0.4)

        # Create lines
        minline = Line(ax.c2p(Min, box_start), ax.c2p(Min, box_start + box_height), color="#ffa600")
        q1line = Line(ax.c2p(q1, box_start), ax.c2p(q1, box_start + box_height), color="#ffa600")
        q2line = Line(ax.c2p(q2, box_start), ax.c2p(q2, box_start + box_height), color="#ffa600")
        q3line = Line(ax.c2p(q3, box_start), ax.c2p(q3, box_start + box_height), color="#ffa600")
        maxline=Line(ax.c2p(Max, box_start), ax.c2p(Max, box_start + box_height), color="#ffa600")
        lower_whisker = Line(minline.get_midpoint(), ax.c2p(q1, box_start + box_height/2), color="#ffa600")
        upper_whisker = Line(maxline.get_midpoint(), ax.c2p(q3, box_start + box_height/2), color="#ffa600")


        # Create labels for statistics
        min_label = MathTex(f"\min={Min}").move_to(LEFT * 4 + UP*2)
        min_diff_label = MathTex(f"\min - \sigma={Minimum}").next_to(min_label, UP)
        max_label = MathTex(f"\max={Max}").next_to(min_label, DOWN)
        max_diff_label = MathTex(f"\max + \sigma={Maximum}").next_to(max_label, DOWN)
        #mean_label = MathTex(f"\mean={Mean}").next_to(min_diff_label, UP)

        q1_label = MathTex(f"Q1={q1}").next_to(q1line, UP)
        q2_label = MathTex(f"Q3={q2}").next_to(q1_label, DOWN)
        q3_label = MathTex(f"Q3={q3}").next_to(q2_label, DOWN)
        range_label = MathTex(f"Q3 - Q1={quartilerange}").next_to(q3_label, DOWN)


        # Add the polygon and lines to the scene
        #self.add(box,minline,midline,maxline,lower_whisker,upper_whisker)
        #self.add(q1_label,q2_label,q3_label)
        self.play(Indicate(dataT[0][8:10]),Write(q2line))
        self.wait(2)
        self.play(Indicate(dataT[0][3:4]),Write(q1line))
        self.wait(2)
        self.play(Indicate(dataT[0][14:16]),Write(q3line))
        self.wait(2)
        self.play(Write(box))
        self.wait(2)
        self.play(Indicate(dataT[0][1]),Write(minline),Write(lower_whisker))
        self.wait(2)
        self.play(Indicate(dataT[0][17:19]),Write(maxline),Write(upper_whisker))
        self.wait(2)
        self.play(FadeOut(box,q2line,q1line,q3line,minline,maxline,lower_whisker,upper_whisker,ax,dataT))
        self.wait(1)




        data = [12, 0, 9, 4, 15, 2, 6, 10, 27, 15, 5, 9, 1, 14, 2]
        dataT = Tex(data).to_edge(UP)

        # Calculate statistics
        Min= int(np.min(data))
        Minimum= int((np.min(data))-(0.2*(np.max(data)-np.min(data))))
        Max= int(np.max(data))
        Maximum= int((np.max(data))+(0.2*(np.max(data)-np.min(data))))
        q1 = int(np.percentile(data, 25, interpolation='lower'))
        q2 = int(np.percentile(data, 50, interpolation='nearest'))
        q3 = int(np.percentile(data, 75, interpolation='higher'))

        quartilerange = q3 - q1

        #defining axes
        ax = AxesWithoutY(
            x_range=(Minimum, Maximum),
            y_range=(0, 6),
            #x_length=8,
            tips=False,
            axis_config={
            "include_numbers": True,
            "numbers_to_include": [Min, q1, q2, q3, Max],
            "numbers_with_elongated_ticks": [Min, q1, q2, q3, Max],
                        },  
                )
        
        # Add labels to the scene
        #self.add(min_label, max_label, q1_label, q2_label, q3_label)
        self.add(ax)
        self.add(dataT)
        self.wait()
        data.sort()
        dataT2 = Tex(data).to_edge(UP)
        self.play(ReplacementTransform(dataT,dataT2))
        self.wait()

        # Calculate width and height of the polygon
        box_start = 1
        box_height = 1.5
        
        # Calculate coordinates for the polygon vertices
        vertices = [
            ax.c2p(q1, box_start),           # bottom-left corner
            ax.c2p(q3, box_start),           # bottom-right corner
            ax.c2p(q3, box_start+box_height),  # top-right corner
            ax.c2p(q1, box_start+box_height),  # top-left corner
        ]

        # Create the polygon
        box = Polygon(*vertices, color="#ffa600", fill_opacity=0.4)

        # Create lines
        minline = Line(ax.c2p(Min, box_start), ax.c2p(Min, box_start + box_height), color="#ffa600")
        q1line = Line(ax.c2p(q1, box_start-0.1), ax.c2p(q1, box_start + box_height+0.1), color=PURE_RED)
        q2line = Line(ax.c2p(q2, box_start-0.1), ax.c2p(q2, box_start + box_height+0.1), color=PURE_RED)
        q3line = Line(ax.c2p(q3, box_start-0.1), ax.c2p(q3, box_start + box_height+0.1), color=PURE_RED)
        maxline=Line(ax.c2p(Max, box_start), ax.c2p(Max, box_start + box_height), color="#ffa600")
        lower_whisker = Line(minline.get_midpoint(), ax.c2p(q1, box_start + box_height/2), color="#ffa600")
        upper_whisker = Line(maxline.get_midpoint(), ax.c2p(q3, box_start + box_height/2), color="#ffa600")



        q2linetop = Line((dataT[0][15].get_top()+UP*0.2),(dataT[0][15].get_bottom()+DOWN*0.2), color=PURE_RED)
        q2text=Tex("q2", color=PURE_RED).next_to(q2linetop, DOWN)
        q2num=Tex("9").next_to(q2text, DOWN)
        self.play(Write(q2linetop))
        self.wait()
        self.play(Write(q2text),Write(q2num))
        
        self.wait(2)
        self.play(Indicate(dataT[0][15]),Write(q2line))
        self.wait()
        

        verticesL = [
            (dataT[0][0].get_left()+DOWN*0.3),           # bottom-left corner
            (dataT[0][13].get_right()+DOWN*0.3),           # bottom-right corner
            (dataT[0][13].get_right()+UP*0.3),  # top-right corner
            (dataT[0][0].get_left()+UP*0.3),  # top-left corner
        ]
        leftbox = Polygon(*verticesL, color="#ffa600", fill_opacity=0.1)

        verticesR = [
            (dataT[0][17].get_left()+DOWN*0.3),           # bottom-left corner
            (dataT[0][-1].get_right()+DOWN*0.3),           # bottom-right corner
            (dataT[0][-1].get_right()+UP*0.3),  # top-right corner
            (dataT[0][17].get_left()+UP*0.3),  # top-left corner
        ]

        rightbox = Polygon(*verticesR, color="#ffa600", fill_opacity=0.1)

        self.play(Write(leftbox))
        q1linetop = Line((dataT[0][7].get_top()+UP*0.2),(dataT[0][7].get_bottom()+DOWN*0.2), color=PURE_RED)
        q1text=Tex("q1", color=PURE_RED).next_to(q1linetop, DOWN)
        q1num=Tex("2").next_to(q1text, DOWN)
        self.wait()
        self.play(Write(q1linetop))
        self.wait()
        self.play(Write(q1text),Write(q1num))
        self.wait(2)
        self.play(Indicate(dataT[0][7]),Write(q1line))
        self.wait()

        self.play(Write(rightbox))
        q3linetop = Line((dataT[0][25:27].get_top()+UP*0.2),(dataT[0][25:27].get_bottom()+DOWN*0.2), color=PURE_RED)
        q3text=Tex("q3", color=PURE_RED).next_to(q3linetop, DOWN)
        q3num=Tex("14").next_to(q3text, DOWN)
        self.wait()
        self.play(Write(q3linetop))
        self.wait()
        self.play(Write(q3text),Write(q3num))

        self.wait(2)
        self.play(Indicate(dataT[0][25:27]),Write(q3line))
        self.wait()


        self.wait(2)
        self.play(Write(box))
        self.wait(2)
        self.play(Indicate(dataT[0][1]),Write(minline),Write(lower_whisker))
        self.wait(2)
        self.play(Indicate(dataT[0][-3:-1]),Write(maxline),Write(upper_whisker))

        self.wait(4)
        self.play(FadeOut(q2line,q1line,q3line,box,minline,lower_whisker,maxline,upper_whisker,ax))
        self.wait()
        #
        # Scene 2 with new numbaz (even)
        #

        data2 = [6, 9, 10, 12, 14, 15, 18, 27]
        dataT2 = Tex(data2).to_edge(UP).shift(DOWN*4)
        self.play(Write(dataT2))
        
        q2linebottom = Line((dataT2[0][8:13].get_top()+UP*0.2),(dataT2[0][8:13].get_bottom()+DOWN*0.2), color=PURE_RED)
        q2text2=Tex("q2", color=PURE_RED).next_to(q2linebottom, DOWN)
        q2num2=Tex("13").next_to(q2text2, DOWN)
        self.play(Write(q2linebottom))
        self.wait()
        self.play(Write(q2text2),(Write(q2num2)))
        self.wait()
        
        

        verticesL2 = [
            (dataT2[0][0].get_left()+DOWN*0.3),            # bottom-left corner
            (dataT2[0][9].get_right()+DOWN*0.3),           # bottom-right corner
            (dataT2[0][9].get_right()+UP*0.3),             # top-right corner
            (dataT2[0][0].get_left()+UP*0.3),              # top-left corner
        ]
        leftbox2 = Polygon(*verticesL2, color="#ffa600", fill_opacity=0.1)

        verticesR2 = [
            (dataT2[0][11].get_left()+DOWN*0.3),            # bottom-left corner
            (dataT2[0][-1].get_right()+DOWN*0.3),           # bottom-right corner
            (dataT2[0][-1].get_right()+UP*0.3),             # top-right corner
            (dataT2[0][11].get_left()+UP*0.3),              # top-left corner
        ]

        rightbox2 = Polygon(*verticesR2, color="#ffa600", fill_opacity=0.1)

        self.play(Write(leftbox2))
        q1linebottom = Line((dataT2[0][3:7].get_top()+UP*0.2),(dataT2[0][3:7].get_bottom()+DOWN*0.2), color=PURE_RED)
        q1text2=Tex("q1", color=PURE_RED).next_to(q1linebottom, DOWN)
        q1num2=Tex("9.5").next_to(q1text2, DOWN)
        self.wait()
        self.play(Write(q1linebottom))
        self.wait()
        self.play(Write(q1text2),Write(q1num2))
        self.wait()

        self.play(Write(rightbox2))
        q3linebottom = Line((dataT2[0][14:19].get_top()+UP*0.2),(dataT2[0][14:19].get_bottom()+DOWN*0.2), color=PURE_RED)
        q3text2=Tex("q3", color=PURE_RED).next_to(q3linebottom, DOWN)
        q3num2=Tex("16.5").next_to(q3text2, DOWN)
        self.wait()
        self.play(Write(q3linebottom))
        self.wait()
        self.play(Write(q3text2),Write(q3num2))
        self.wait(8)