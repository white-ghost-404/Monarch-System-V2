from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton

class MonarchApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        
        # Player Stats: LVL 1 | RANK E
        self.level = 1
        self.rank = "E-RANK"
        
        screen = MDScreen()
        
        # UI Design for Elite Status
        card = MDCard(
            orientation='vertical', padding="20dp", size_hint=(0.85, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            line_color=(0, 0.95, 1, 1), md_bg_color=(0, 0, 0, 1), elevation=4
        )
        
        self.status = MDLabel(
            text=f"RANK: {self.rank}\nLEVEL: {self.level}",
            halign="center", theme_text_color="Custom", text_color=(0, 0.95, 1, 1),
            font_style="H5"
        )
        
        self.quest = MDLabel(
            text=f"CURRENT QUEST:\nLift 1KG / Run 1KM",
            halign="center", theme_text_color="Secondary"
        )
        
        card.add_widget(self.status)
        card.add_widget(self.quest)
        
        # Action Button
        btn = MDRaisedButton(
            text="COMPLETE MISSION", pos_hint={"center_x": 0.5, "center_y": 0.25},
            on_release=self.evolve
        )
        
        screen.add_widget(card)
        screen.add_widget(btn)
        return screen

    def evolve(self, *args):
        self.level += 1
        # Progression Logic
        if self.level > 10: self.rank = "D-RANK"
        if self.level > 50: self.rank = "B-RANK"
        if self.level > 150: self.rank = "S-RANK"
        
        self.status.text = f"RANK: {self.rank}\nLEVEL: {self.level}"
        self.quest.text = f"CURRENT QUEST:\nLift {self.level}KG / Run {self.level}KM"

MonarchApp().run()
