;; Auto-generated. Do not edit!


(when (boundp 'turtle_battle::GameState)
  (if (not (find-package "TURTLE_BATTLE"))
    (make-package "TURTLE_BATTLE"))
  (shadow 'GameState (find-package "TURTLE_BATTLE")))
(unless (find-package "TURTLE_BATTLE::GAMESTATE")
  (make-package "TURTLE_BATTLE::GAMESTATE"))

(in-package "ROS")
;;//! \htmlinclude GameState.msg.html


(defclass turtle_battle::GameState
  :super ros::object
  :slots (_turtle1_health _turtle2_health _turtle1_attacks_remaining _turtle2_attacks_remaining ))

(defmethod turtle_battle::GameState
  (:init
   (&key
    ((:turtle1_health __turtle1_health) 0)
    ((:turtle2_health __turtle2_health) 0)
    ((:turtle1_attacks_remaining __turtle1_attacks_remaining) 0)
    ((:turtle2_attacks_remaining __turtle2_attacks_remaining) 0)
    )
   (send-super :init)
   (setq _turtle1_health (round __turtle1_health))
   (setq _turtle2_health (round __turtle2_health))
   (setq _turtle1_attacks_remaining (round __turtle1_attacks_remaining))
   (setq _turtle2_attacks_remaining (round __turtle2_attacks_remaining))
   self)
  (:turtle1_health
   (&optional __turtle1_health)
   (if __turtle1_health (setq _turtle1_health __turtle1_health)) _turtle1_health)
  (:turtle2_health
   (&optional __turtle2_health)
   (if __turtle2_health (setq _turtle2_health __turtle2_health)) _turtle2_health)
  (:turtle1_attacks_remaining
   (&optional __turtle1_attacks_remaining)
   (if __turtle1_attacks_remaining (setq _turtle1_attacks_remaining __turtle1_attacks_remaining)) _turtle1_attacks_remaining)
  (:turtle2_attacks_remaining
   (&optional __turtle2_attacks_remaining)
   (if __turtle2_attacks_remaining (setq _turtle2_attacks_remaining __turtle2_attacks_remaining)) _turtle2_attacks_remaining)
  (:serialization-length
   ()
   (+
    ;; int32 _turtle1_health
    4
    ;; int32 _turtle2_health
    4
    ;; int32 _turtle1_attacks_remaining
    4
    ;; int32 _turtle2_attacks_remaining
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _turtle1_health
       (write-long _turtle1_health s)
     ;; int32 _turtle2_health
       (write-long _turtle2_health s)
     ;; int32 _turtle1_attacks_remaining
       (write-long _turtle1_attacks_remaining s)
     ;; int32 _turtle2_attacks_remaining
       (write-long _turtle2_attacks_remaining s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _turtle1_health
     (setq _turtle1_health (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _turtle2_health
     (setq _turtle2_health (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _turtle1_attacks_remaining
     (setq _turtle1_attacks_remaining (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _turtle2_attacks_remaining
     (setq _turtle2_attacks_remaining (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get turtle_battle::GameState :md5sum-) "0051aa3ff6623e54a13e3a5509f76a87")
(setf (get turtle_battle::GameState :datatype-) "turtle_battle/GameState")
(setf (get turtle_battle::GameState :definition-)
      "int32 turtle1_health
int32 turtle2_health
int32 turtle1_attacks_remaining
int32 turtle2_attacks_remaining

")



(provide :turtle_battle/GameState "0051aa3ff6623e54a13e3a5509f76a87")


