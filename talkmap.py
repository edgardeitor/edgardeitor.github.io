# Leaflet cluster map of talk locations
#
# Run this from the repository root (the folder that contains _talks/). It reads
# the location field of every .md file in _talks/, geocodes each distinct place
# once with geopy/Nominatim (slowly, as Nominatim's usage policy requires, and
# with retries), and uses getorg to write the map into the talkmap/ folder.
import glob
import frontmatter
import getorg
from geopy import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# Collect the Markdown files
g = sorted(glob.glob("_talks/*.md"))

# Prepare to geolocate: at most one request per second, a few retries on errors
geocoder = Nominatim(user_agent="edgardeitor.github.io", timeout=10)
geocode = RateLimiter(
    geocoder.geocode,
    min_delay_seconds=1.2,
    max_retries=4,
    error_wait_seconds=10,
    swallow_exceptions=True,
    return_value_on_exception=None,
)

place_cache = {}      # each distinct location is looked up only once
location_dict = {}
failed = []

for file in g:
    data = frontmatter.load(file).to_dict()

    # Press on if the location is not present
    if "location" not in data:
        continue

    title = data["title"].strip()
    venue = data["venue"].strip()
    location = data["location"].strip()
    description = f"{title}<br />{venue}; {location}"

    if location not in place_cache:
        place_cache[location] = geocode(location)
        if place_cache[location] is None:
            print(f"Error: could not geocode '{location}'")
    result = place_cache[location]

    if result is None:
        failed.append((file, location))
        continue

    location_dict[description] = result
    print(description, result)

print(f"\nPlotted {len(location_dict)} talks; {len(failed)} could not be placed.")
for file, location in failed:
    print(f"  not placed: {file} ({location})")

# Save the map
getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="talkmap", hashed_usernames=False)

# Fail the run if some talks are missing, so an incomplete map is never committed silently
if failed:
    raise SystemExit(1)
