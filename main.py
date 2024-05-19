# Track class
class Track:
    def __init__(self, name, artist, genre, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.danceability = self._convert_to_float(danceability)
        self.energy = self._convert_to_float(energy)
        self.key = self._convert_to_int(key)
        self.loudness = self._convert_to_float(loudness)
        self.mode = self._convert_to_int(mode)
        self.speechiness = self._convert_to_float(speechiness)
        self.acousticness = self._convert_to_float(acousticness)
        self.instrumentalness = self._convert_to_float(instrumentalness)
        self.liveness = self._convert_to_float(liveness)
        self.valence = self._convert_to_float(valence)
        self.tempo = self._convert_to_float(tempo)
        self.duration = self._convert_to_int(duration)

    # Validation float
    def _convert_to_float(self, value):
        try:
            return float(value)
        except ValueError:
            return None

    # Validation int
    def _convert_to_int(self, value):
        try:
            return int(value)
        except ValueError:
            return None

    # Show data
    def __repr__(self):
        return (f"Track(name={self.name}, artist={self.artist}, genre={self.genre}, danceability={self.danceability}, "
                f"energy={self.energy}, key={self.key}, loudness={self.loudness}, mode={self.mode}, speechiness={self.speechiness}, "
                f"acousticness={self.acousticness}, instrumentalness={self.instrumentalness}, liveness={self.liveness}, "
                f"valence={self.valence}, tempo={self.tempo}, duration={self.duration})")

# Get track list
def create_track_list(file_path):
    track_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = []
            variable = ""
            is_quotes = False

            for char in line:
                if char == '"':
                    is_quotes = not is_quotes
                if char == ',' and not is_quotes:
                    data.append(variable)
                    variable = ''
                else:
                    variable += char

            data.append(variable)

            track = Track(
                name=data[1],
                artist=data[2],
                genre=data[9],
                danceability=data[11],
                energy=data[12],
                key=data[13],
                loudness=data[14],
                mode=data[15],
                speechiness=data[16],
                acousticness=data[17],
                instrumentalness=data[18],
                liveness=data[19],
                valence=data[20],
                tempo=data[21],
                duration=data[22]
            )
            track_list.append(track)
    return track_list

# Get unique genres
def get_genres(tracks):
    genres = set()
    for track in tracks:
        if track.genre:
            genres.add(track.genre)
    return list(genres)

# Get data
track_list = create_track_list('Tracks.txt')

genres = get_genres(track_list)
print(genres)