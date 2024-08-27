// Auto-generated. Do not edit!

// (in-package turtle_battle.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class GameState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.turtle1_health = null;
      this.turtle2_health = null;
      this.turtle1_attacks_remaining = null;
      this.turtle2_attacks_remaining = null;
    }
    else {
      if (initObj.hasOwnProperty('turtle1_health')) {
        this.turtle1_health = initObj.turtle1_health
      }
      else {
        this.turtle1_health = 0;
      }
      if (initObj.hasOwnProperty('turtle2_health')) {
        this.turtle2_health = initObj.turtle2_health
      }
      else {
        this.turtle2_health = 0;
      }
      if (initObj.hasOwnProperty('turtle1_attacks_remaining')) {
        this.turtle1_attacks_remaining = initObj.turtle1_attacks_remaining
      }
      else {
        this.turtle1_attacks_remaining = 0;
      }
      if (initObj.hasOwnProperty('turtle2_attacks_remaining')) {
        this.turtle2_attacks_remaining = initObj.turtle2_attacks_remaining
      }
      else {
        this.turtle2_attacks_remaining = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GameState
    // Serialize message field [turtle1_health]
    bufferOffset = _serializer.int32(obj.turtle1_health, buffer, bufferOffset);
    // Serialize message field [turtle2_health]
    bufferOffset = _serializer.int32(obj.turtle2_health, buffer, bufferOffset);
    // Serialize message field [turtle1_attacks_remaining]
    bufferOffset = _serializer.int32(obj.turtle1_attacks_remaining, buffer, bufferOffset);
    // Serialize message field [turtle2_attacks_remaining]
    bufferOffset = _serializer.int32(obj.turtle2_attacks_remaining, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GameState
    let len;
    let data = new GameState(null);
    // Deserialize message field [turtle1_health]
    data.turtle1_health = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [turtle2_health]
    data.turtle2_health = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [turtle1_attacks_remaining]
    data.turtle1_attacks_remaining = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [turtle2_attacks_remaining]
    data.turtle2_attacks_remaining = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'turtle_battle/GameState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0051aa3ff6623e54a13e3a5509f76a87';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 turtle1_health
    int32 turtle2_health
    int32 turtle1_attacks_remaining
    int32 turtle2_attacks_remaining
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GameState(null);
    if (msg.turtle1_health !== undefined) {
      resolved.turtle1_health = msg.turtle1_health;
    }
    else {
      resolved.turtle1_health = 0
    }

    if (msg.turtle2_health !== undefined) {
      resolved.turtle2_health = msg.turtle2_health;
    }
    else {
      resolved.turtle2_health = 0
    }

    if (msg.turtle1_attacks_remaining !== undefined) {
      resolved.turtle1_attacks_remaining = msg.turtle1_attacks_remaining;
    }
    else {
      resolved.turtle1_attacks_remaining = 0
    }

    if (msg.turtle2_attacks_remaining !== undefined) {
      resolved.turtle2_attacks_remaining = msg.turtle2_attacks_remaining;
    }
    else {
      resolved.turtle2_attacks_remaining = 0
    }

    return resolved;
    }
};

module.exports = GameState;
