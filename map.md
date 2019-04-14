#!/usr/bin/env python

pints = {
    "heinz": {
        "sven": ["forward", "forward"],
        "milo": ["right", "right"],
        "claudio": ["forward", "right", "left"],
        "start": ["forward", "right", "forward"],
        "chruch": ["left"],
        "cinema": ["forward", "left"],
        "lake": ["right", "forward"]
    }

    "milo": {
        "sven": ["forward", "left", "right"],
        "claudio": ["forward", "forward"],
        "heinz": ["left", "left"],
        "start": ["forward", "right"],
        "church": ["left", "forward"],
        "cinema": ["forward", "left", "forward"],
        "lake": ["right"]
    }

    "sven": {
        "milo": ["forward", "left", "right"],
        "claudio": ["left", "left"],
        "heinz": ["forward", "forward"],
        "start": ["left", "forward"],
        "church": ["forward", "right"],
        "cinema": ["right"],
        "lake": ["forward", "left", "forward"]
    }

    "claudio": {
        "sven": ["right", "right"],
        "milo": ["forward", "forward"],
        "heinz": ["forward", "right", "left"],
        "start": ["left"],
        "church": ["forward", "right", "forward"],
        "cinema": ["right", "forward"],
        "lake": ["forward", "left"]
    }

    "start": {
        "sven": ["forward", "right"],
        "milo": ["left", "forward"],
        "claudio": ["right"],
        "heinz": ["froward", "left", "forward"],
        "church": ["forward", "left", "right"],
        "cinema": ["forard", "forward"],
        "lake": ["left", "left"]
    }

    "church": {
        "sven": ["left", "forward"],
        "milo": ["forward", "right"],
        "claudio": ["forward", "left", "forward"],
        "heinz": ["right"],
        "start": ["forward", "left", "right"],
        "cinema": ["left", "left"],
        "lake": ["forward", "forward"]
    }

    "cinema": {
        "sven": ["left"],
        "milo": ["forward", "right", "forward"],
        "claudio": ["forward", "left"],
        "heinz": ["right", "forward"],
        "start": ["forward", "forward"],
        "church": ["right", "right"],
        "lake": ["forward", "right", "left"]
    }

    "lake": {
        "sven": ["forward", "right", "forward"],
        "milo": ["left"],
        "claudio": ["right", "forward"],
        "heinz": ["forward", "left"],
        "start": ["right", "right"],
        "church": ["forward", "forward"],
        "cinema": ["forward", "right", "left"]
    }
}



