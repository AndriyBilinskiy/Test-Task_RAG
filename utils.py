import ast
def format_cocktail_row_to_string(row):
    """Formats a cocktail entry into a retrievable text chunk."""
    ingredients = ''
    ingreds, measures = ast.literal_eval(row['ingredients']), ast.literal_eval(row['ingredientMeasures'])
    for i in range(len(ingreds)):
        try:
            ingredients += f" {ingreds[i]} ({measures[i]}),"
        except:
            pass
    ingredients = ingredients[:-1]
    return f"The cocktail name is {row['name']}, its {row['alcoholic']}, the category of the cocktail is {row['category']},  it is served in {row['glassType']}\nIngredients: {ingredients}.\nPreparation:{row['instructions']}"

def read_and_format_cocktails(file_path):
    import pandas as pd
    df = pd.read_csv(file_path, index_col=0)
    df.dropna(inplace=True)
    texts = df.apply(format_cocktail_row_to_string, axis=1).tolist()
    return texts

def form_prompt(query, retrieved_text):
    prompt = f"""
        You are a world-class cocktail expert. Answer the user's question based on the most relevant cocktails from cocktail database.

        ### Most relevant cocktails:
        {retrieved_text}

        ### Instructions:
        - Only use the provided context.
        - If the answer is not in the context, say "I don't have enough information."
        - Format your answer in a clear, structured way.

        ### Example Response:
        Question: What are 5 cocktails containing lemon?
        Answer:
        - **Whiskey Sour**: Whiskey, Lemon Juice, Sugar
        - **Tom Collins**: Gin, Lemon Juice, Soda Water, Sugar
        - **Bee's Knees**: Gin, Lemon Juice, Honey
        - **Sidecar**: Cognac, Lemon Juice, Triple Sec
        - **Lemon Drop Martini**: Vodka, Lemon Juice, Triple Sec, Sugar Rim

        Question: {query}
        """
    return prompt
