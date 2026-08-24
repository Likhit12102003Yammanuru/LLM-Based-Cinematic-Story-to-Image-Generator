import spacy

from app.scene_parser import parse_scene
from app.prompt_generator import generate_prompt
from app.llm_enricher import enrich_scene_with_llm
from app.shot_planner import choose_shot
from app.pronoun_resolver import resolve_pronouns

nlp = spacy.load("en_core_web_sm")

def process_story(text, context_manager):

    doc = nlp(text)

    scenes = []

    scene_id = 1

    for sent in doc.sents:

        sentence_text = sent.text.strip()

        # Parse scene
        scene = parse_scene(sentence_text)

        # Resolve pronouns
        scene = resolve_pronouns(
            scene,
            sentence_text,
            context_manager.context
        )

        # Context continuity
        scene = context_manager.enrich_scene(
            scene,
            sentence_text
        )

        # Update memory
        context_manager.update_context(scene)

        # LLM cinematic enrichment
        llm_data = enrich_scene_with_llm(
            scene,
            sentence_text
        )

        # Cinematic shot planning
        llm_data["camera"] = choose_shot(scene_id)

        # Generate final prompt
        prompt = generate_prompt(
            scene,
            llm_data
        )

        scenes.append({
            "scene_id": scene_id,
            "text": sentence_text,
            "scene": scene,
            "llm_enrichment": llm_data,
            "prompt": prompt
        })

        scene_id += 1

    return scenes

