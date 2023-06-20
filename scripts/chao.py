from pyodide import JsException
from pyodide.http import pyfetch

async def wiki_summary(slug):

    try:
        response = await pyfetch(
            url=f"https://en.wikipedia.org/api/rest_v1/page/summary/{slug}",
            method='GET',
            headers={'Content-Type': 'application/json'}
        )
        if response.ok:
            data = await response.json()
            return data
    except JsException:
        return None

async def get_summary(slug):
    summary = await wiki_summary(slug)
    if summary is None:
        return f"""
            <h1>no results found. try again.</h1>
            <p>Wikipedia doesn't have an entry for {slug}. either that, or chao is confused! </p>
            """
    else:
        output = f"""
            <h1>{summary['title']}</h1>
            <p>{summary['extract_html']}</p>
            """

        return output