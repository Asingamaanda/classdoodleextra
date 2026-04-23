# ClassDoodle Chemical Equilibrium (Grade 12)

Cinematic, learner-friendly Manim lesson for:
- Dynamic chemical equilibrium
- Le Chatelier's Principle
- Concentration, pressure, temperature, and catalyst effects
- Exam method + worked practice logic

## Project Structure

- `main.py` – exports all renderable scene classes
- `scenes/components.py` – reusable visual components
  - `ParticleBox`
  - `ReactionEquation`
  - `EquilibriumGraph`
  - `ShiftArrow`
  - `ExamTable`
- `scenes/lesson_scenes.py` – Scene 1 to Scene 12
- `assets/` – optional local assets (currently placeholder folder)
- `lesson_timeline.json` – narration/action/pause map
- `blender_concept.md` – optional Blender production approach

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Render Commands

Render one scene quickly:

```bash
manim -pqh main.py Scene1TitleHook
```

Render exam method scene:

```bash
manim -pqh main.py Scene10ExamMethod
```

Render a higher quality scene:

```bash
manim -p -qh main.py Scene12FinalRecap
```

Render all lesson scenes (bash loop):

```bash
for s in \
  Scene1TitleHook Scene2DynamicEquilibrium Scene3RateVsTimeGraph Scene4LeChatelier \
  Scene5ConcentrationChange Scene6PressureChange Scene7TemperatureChange Scene8Catalyst \
  Scene9ExperimentVisualiser Scene10ExamMethod Scene11PracticeQuestion Scene12FinalRecap; do
  manim -pqh main.py "$s"
done
```

## Style Notes

- Dark cinematic background
- Blue / white / gold accents
- Large text for classroom readability
- Built for voiceover pacing with explicit narration comments in each scene

## Optional Blender Upgrade

See `blender_concept.md` for a practical 3D pipeline while keeping this repo lightweight.
