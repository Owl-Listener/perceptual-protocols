# Example: Folk Maximalism

This is a complete working example of mood-protocol in action.

## What's here

```
folk-maximalism/
  mood/
    moodboard-01.png    ← Pinterest board screenshot (page 1)
    moodboard-02.png    ← Pinterest board screenshot (page 2)
    notes.md            ← designer's freeform annotations
  mood.md               ← generated output
```

## How it was made

1. A designer collected references on a Pinterest board — folk art, block prints, linocut illustrations, hand-lettered type, creature-dense compositions
2. They took two screenshots of the board
3. They wrote a short `notes.md` with their thoughts on the direction
4. They ran: `python generate_mood.py --input ./examples/folk-maximalism/mood --output ./examples/folk-maximalism --name "Folk Maximalism"`
5. The generated `mood.md` is the result

## Try it yourself

You can regenerate this example to see how different models interpret the same moodboard:

```bash
# With Claude
python generate_mood.py --input ./examples/folk-maximalism/mood --output ./examples/folk-maximalism --name "Folk Maximalism"

# With Gemini
python generate_mood.py --model gemini --input ./examples/folk-maximalism/mood --output ./examples/folk-maximalism --name "Folk Maximalism"
```

Compare the outputs. The same images produce subtly different readings from different models — which is itself an interesting design conversation.

## What to notice

Open `mood.md` and look at:

- **Colour** — Did the model extract accurate hex values from the references?
- **Typography** — How well did it capture the hand-lettered character?
- **Emotional Register** — Does the description match what you feel looking at the images?
- **Anti-References** — Are the "things to avoid" useful and specific?
- **Agent Instructions** — Could you hand this to an AI and get better design output?

Then look at what's missing. That gap is where your expertise as a designer fills in. Edit the mood file. Make it yours. The generated version is a starting point, not a final deliverable.
