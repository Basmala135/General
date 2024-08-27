;; Auto-generated. Do not edit!


(when (boundp 'turtle_battle::AttackCommand)
  (if (not (find-package "TURTLE_BATTLE"))
    (make-package "TURTLE_BATTLE"))
  (shadow 'AttackCommand (find-package "TURTLE_BATTLE")))
(unless (find-package "TURTLE_BATTLE::ATTACKCOMMAND")
  (make-package "TURTLE_BATTLE::ATTACKCOMMAND"))

(in-package "ROS")
;;//! \htmlinclude AttackCommand.msg.html


(defclass turtle_battle::AttackCommand
  :super ros::object
  :slots ())

(defmethod turtle_battle::AttackCommand
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(setf (get turtle_battle::AttackCommand :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get turtle_battle::AttackCommand :datatype-) "turtle_battle/AttackCommand")
(setf (get turtle_battle::AttackCommand :definition-)
      "
")



(provide :turtle_battle/AttackCommand "d41d8cd98f00b204e9800998ecf8427e")


