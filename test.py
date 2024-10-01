import pickle

with open('stubs/track_stubs.pkl', 'rb') as f:
    tracks = pickle.load(f)

print(f"Total frames in stub: {len(tracks['player'])}")